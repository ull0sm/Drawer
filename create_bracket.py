import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def read_excel_sheets(file_path):
    """
    Read all sheets from an Excel file and return a dictionary of player lists.
    Each sheet corresponds to a key (sheet name) with its respective player list.
    """
    sheets = pd.read_excel(file_path, sheet_name=None)
    sheet_players = {sheet_name: data.iloc[:, 0].dropna().tolist() for sheet_name, data in sheets.items()}
    return sheet_players


def create_bracket(players):
    """
    Arrange players into a single-elimination bracket structure.
    Adds "BYE" slots to ensure the total number of players is a power of 2.
    """
    while len(players) & (len(players) - 1) != 0:  # Ensure power of 2
        players.append("BYE")
    return players


def draw_bracket(sheet_name, players, pdf):
    """
    Draw the tournament bracket for the given players and save it as a page in the PDF.
    """
    num_players = len(players)
    num_rounds = num_players.bit_length() - 1

    # Calculate spacing
    match_height = 1.5
    round_width = 3

    fig, ax = plt.subplots(figsize=(num_rounds * round_width, num_players * match_height / 2))
    ax.set_xlim(0, num_rounds * round_width)
    ax.set_ylim(0, num_players * match_height)
    ax.axis("off")

    positions = []

    # Draw the title
    fig.suptitle(f"Single Elimination Draw - {sheet_name}", fontsize=14, weight='bold', y=0.92)

    # Draw initial round
    for i, player in enumerate(players):
        x = 0
        y = i * match_height
        ax.text(x, y, player, ha="right", va="center", fontsize=8, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black"))
        positions.append((x, y))

    # Draw subsequent rounds
    current_positions = positions
    for round_idx in range(1, num_rounds + 1):
        next_positions = []
        for i in range(0, len(current_positions), 2):
            x = round_idx * round_width
            y = (current_positions[i][1] + current_positions[i + 1][1]) / 2

            # Draw connecting lines
            ax.plot([current_positions[i][0], x], [current_positions[i][1], y], color="black")
            ax.plot([current_positions[i + 1][0], x], [current_positions[i + 1][1], y], color="black")

            # Add placeholder for the winner
            ax.text(x, y, "", ha="center", va="center", fontsize=8, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black"))
            next_positions.append((x, y))

        current_positions = next_positions

    # Save the figure to the PDF
    pdf.savefig(fig)
    plt.close(fig)


def main():
    input_excel = "grouped_output.xlsx"  # Replace with your Excel file path
    output_pdf = "multi_page_tournament_bracket.pdf"

    # Read all sheets and their players
    sheet_players = read_excel_sheets(input_excel)

    # Open a PDF file for multi-page output
    with PdfPages(output_pdf) as pdf:
        for sheet_name, players in sheet_players.items():
            players = create_bracket(players)  # Ensure power of 2
            draw_bracket(sheet_name, players, pdf)

    print(f"Multi-page tournament bracket saved to {output_pdf}")


if __name__ == "__main__":
    main()