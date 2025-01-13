import pandas as pd
import random
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

# Step 1: Read the Excel file
file_path = "trial.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path)

# Step 2: Group players into sets of 8
def group_players(df, group_size=8):
    groups = [df.iloc[i:i+group_size] for i in range(0, len(df), group_size)]
    return groups

groups = group_players(df)

# Step 3: Generate Single Elimination Bracket
def generate_bracket(group):
    players = group.sample(frac=1).reset_index(drop=True)
    bracket = []
    while len(players) > 1:
        match = players.iloc[:2]
        bracket.append(match)
        players = players.iloc[2:].reset_index(drop=True)
    return bracket

brackets = [generate_bracket(group) for group in groups]

# Step 4: Create PDF Bracket in A4 Landscape Mode
def draw_bracket(c, bracket, x, y, round_num):
    match_height = 40
    for i, match in enumerate(bracket):
        c.drawString(x, y - (i * match_height), f"Round {round_num} - Match {i + 1}")
        for j, player in match.iterrows():
            c.drawString(x + 100, y - (i * match_height) - (j * 15), f"{player['Name']} ({player['School']})")

def create_bracket_pdf(brackets, output_file='bracket.pdf'):
    c = canvas.Canvas(output_file, pagesize=landscape(A4))
    width, height = landscape(A4)
    
    for group_num, bracket in enumerate(brackets):
        x = 50
        y = height - 50 - (group_num * 200)
        for round_num in range(1, 4):
            draw_bracket(c, bracket, x, y, round_num)
            x += 200
            y -= 100
        y -= 100
    
    c.save()

create_bracket_pdf(brackets)