import pandas as pd
import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def read_groups_from_excel(file_path):
    # Read all sheets from the Excel file into a dictionary
    all_sheets = pd.read_excel(file_path, sheet_name=None, usecols=['Number', 'Name', 'School'])
    return all_sheets

def create_single_elimination_bracket(participants):
    rounds = []
    while len(participants) > 1:
        next_round = []
        for i in range(0, len(participants), 2):
            if i + 1 < len(participants):
                next_round.append((participants[i], participants[i + 1]))
            else:
                next_round.append((participants[i], None))  # Bye for odd number of participants
        rounds.append(next_round)
        participants = [winner for match in next_round for winner in match if winner is not None]
    return rounds

def draw_bracket(c, rounds, x, y, width, height):
    for i, round in enumerate(rounds):
        round_height = height / (2 ** (i + 1))
        for j, match in enumerate(round):
            participant1 = f"{match[0]['Number']} - {match[0]['Name']} ({match[0]['School']})" if match[0] else 'Bye'
            participant2 = f"{match[1]['Number']} - {match[1]['Name']} ({match[1]['School']})" if match[1] else ''
            c.drawString(x + i * width, y - j * round_height * 2, participant1)
            if participant2:
                c.drawString(x + i * width, y - j * round_height * 2 - round_height, participant2)

def create_pdf(file_path, groups):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    for group_name, participants in groups.items():
        c.drawString(100, height - 50, f"Group: {group_name}")
        rounds = create_single_elimination_bracket(participants)
        draw_bracket(c, rounds, 100, height - 100, 100, height - 200)
        c.showPage()

    c.save()

def main():
    file_path = "grouped_output.xlsx"
    groups = read_groups_from_excel(file_path)
    
    # Convert DataFrames to lists of dicts
    groups = {group_name: df.to_dict('records') for group_name, df in groups.items()}
    
    output_pdf = 'single_elimination_brackets.pdf'
    create_pdf(output_pdf, groups)
    print(f"Single elimination brackets have been written to {output_pdf}")

if __name__ == "__main__":
    main()