import pandas as pd
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
import os

def draw_bracket(c, players, width, height):
    """Draws a single-elimination bracket with proper pair alignment and alternating colors."""
    
    rounds = [players]  # Initial round with all players

    # Generate rounds by halving the players list until only 1 remains
    while len(rounds[-1]) > 1:
        previous_round = rounds[-1]
        next_round = [f"Winner {i//2 + 1}" for i in range(0, len(previous_round), 2)]
        rounds.append(next_round)
    
    round_count = len(rounds)
    
    box_width = 1.5 * inch
    box_height = 0.5 * inch
    vertical_spacing = 0.8 * inch
    horizontal_spacing = 2.5 * inch

    start_x = 1 * inch
    start_y = height - 1.5 * inch

    # Colors for alternating players
    colors_list = [colors.red, colors.blue]

    # Draw each round
    for round_num, round_players in enumerate(rounds):
        for i, player in enumerate(round_players):
            x = start_x + round_num * horizontal_spacing
            y = start_y - i * vertical_spacing * (2 ** round_num)
            
            # Alternate colors for players
            fill_color = colors_list[i % 2]
            c.setFillColor(fill_color)
            c.setStrokeColor(colors.black)
            c.setLineWidth(1.5)
            
            # Draw the rectangle for the player
            c.rect(x, y, box_width, box_height, stroke=1, fill=1)
            
            # Center the player name in the rectangle
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 10)
            text_width = c.stringWidth(player, "Helvetica-Bold", 10)
            text_x = x + (box_width - text_width) / 2
            text_y = y + (box_height / 2) - 4  # Adjust for text baseline
            c.drawString(text_x, text_y, player)
        
        # Draw connecting lines for the next round
        if round_num < round_count - 1:
            next_round_count = len(rounds[round_num + 1])
            for i in range(0, len(round_players), 2):
                x1 = start_x + round_num * horizontal_spacing + box_width
                y1 = start_y - i * vertical_spacing * (2 ** round_num) + box_height / 2
                
                x2 = x1 + horizontal_spacing
                y2 = start_y - (i // 2) * vertical_spacing * (2 ** (round_num + 1)) + box_height / 2
                
                c.line(x1, y1, x2, y2)

def create_draw_pdf(sheet_name, data, output_folder):
    """Creates a tournament bracket PDF from player data."""
    
    pdf_path = os.path.join(output_folder, f"{sheet_name}_draw.pdf")
    c = canvas.Canvas(pdf_path, pagesize=landscape(A4))
    width, height = landscape(A4)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, f"Single Elimination Draw - {sheet_name}")

    # Extract player names from the DataFrame
    players = data['Name'].tolist()
    
    # Draw the bracket
    draw_bracket(c, players, width, height)

    c.save()
    return pdf_path

def combine_pdfs(pdf_paths, output_pdf):
    from PyPDF2 import PdfMerger

    merger = PdfMerger()
    for pdf in pdf_paths:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()

def main(input_excel, output_pdf):
    output_folder = "temp_draw_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    # Read the Excel file
    xls = pd.ExcelFile(input_excel)

    pdf_paths = []
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        pdf_path = create_draw_pdf(sheet_name, df, output_folder)
        pdf_paths.append(pdf_path)

    combine_pdfs(pdf_paths, output_pdf)

    # Clean up temporary PDFs
    for pdf_path in pdf_paths:
        os.remove(pdf_path)
    os.rmdir(output_folder)

if __name__ == "__main__":
    input_excel = "grouped_outputj.xlsx"
    output_pdf = "combined_draws.pdf"
    main(input_excel, output_pdf)
