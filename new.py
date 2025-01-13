import pandas as pd
import random
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import filedialog, messagebox

# Step 1: Group players into sets of 8
def group_players(df, group_size=8):
    groups = [df.iloc[i:i+group_size] for i in range(0, len(df), group_size)]
    return groups

# Step 2: Generate Single Elimination Bracket
def generate_bracket(group):
    players = group.sample(frac=1).reset_index(drop=True)
    bracket = []
    while len(players) > 1:
        match = players.iloc[:2]
        bracket.append(match)
        players = players.iloc[2:].reset_index(drop=True)
    return bracket

# Step 3: Create PDF Bracket in A4 Landscape Mode
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

# Step 4: Create the UI
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            groups = group_players(df)
            brackets = [generate_bracket(group) for group in groups]
            output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_file:
                create_bracket_pdf(brackets, output_file)
                messagebox.showinfo("Success", "Bracket PDF created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Main application window
root = tk.Tk()
root.title("Bracket Generator")
root.geometry("300x150")

select_button = tk.Button(root, text="Select Excel File", command=select_file)
select_button.pack(pady=20)

root.mainloop()