import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def read_excel_sheets(file_path):
    """
    Read all sheets from an Excel file and return a dictionary of player lists.
    Each sheet corresponds to a key (sheet name) with its respective player list.
    """
    sheets = pd.read_excel(file_path, sheet_name=None)
    sheet_players = {}
    
    for sheet_name, data in sheets.items():
        # Assuming columns: 'Number', 'Name', 'School'
        players = data.dropna(subset=['Name'])  # Remove rows where Name is NaN
        player_info = [
            f"{row['Number']} | {row['Name']}\n{row['School']}"  # Format as "Number | Name" and "School" on the next line
            for _, row in players.iterrows()
        ]
        sheet_players[sheet_name] = player_info

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

    # Aesthetic colors and themes with stronger, bolder hues
    bg_color = "#f4f4f9"  # Light grey background for the whole bracket
    round_color = "#87CEEB"  # Sky blue for rounds
    text_color = "#212121"  # Very dark grey (close to black) for text for readability

    # Stronger, more visible red and blue
    red = "#C62828"  # Bold and deep red (Crimson Red)
    blue = "#1565C0"  # Deep and rich blue
    winner_color = "#32CD32"  # Lime green for winner placeholders

    # Calculate spacing
    match_height = 1.8
    round_width = 4

    fig, ax = plt.subplots(figsize=(num_rounds * round_width, num_players * match_height / 2))
    ax.set_xlim(0, num_rounds * round_width)
    ax.set_ylim(0, num_players * match_height)
    ax.set_facecolor(bg_color)  # Set background color for the entire bracket
    ax.axis("off")

    positions = []

    # Draw the title with a modern font
    fig.suptitle(f"Single Elimination Tournament - {sheet_name}", fontsize=18, weight='bold', y=0.92, color=text_color, family="sans-serif")

    # Draw initial round with alternating colors
    for i, player in enumerate(players):
        x = 0
        y = i * match_height
        color = blue if i % 2 == 0 else red  # Alternate colors with bold and visible red and blue
        # Split the player data into number/name and school
        name, school = player.split("\n")
        ax.text(x, y, name, ha="right", va="center", fontsize=12, color="white",  # Larger font for number/name
                bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor=color, lw=1, alpha=0.9))
        # Display the school name in a smaller font on the next line
        ax.text(x, y - 0.6, school, ha="right", va="center", fontsize=8, color="white",  # Smaller font for school
                bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor=color, lw=1, alpha=0.9))
        positions.append((x, y))

    # Draw subsequent rounds with a winner placeholder at each joint
    current_positions = positions
    for round_idx in range(1, num_rounds + 1):
        next_positions = []
        for i in range(0, len(current_positions), 2):
            # Decide the color for each winner in this round
            if round_idx == num_rounds:
                color = 'green'  # Final winner's box color
            else:
                color = blue if i % 4 == 0 else red  # Alternate colors with bold and visible red and blue

            x = round_idx * round_width
            y = (current_positions[i][1] + current_positions[i + 1][1]) / 2

            # Draw connecting lines
            ax.plot([current_positions[i][0], x], [current_positions[i][1], y], color=color, lw=1)  # this is the color for line
            ax.plot([current_positions[i + 1][0], x], [current_positions[i + 1][1], y], color=color, lw=1) # color for line

            # Add placeholder for the winner with a soft lime green (adjust if necessary)
            ax.text(x, y, "", ha="center", va="center", fontsize=12, color=winner_color,
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor=winner_color, lw=1, alpha=0.4))
            
            # Add "Winner" box at each intersection with updated color
            ax.text(x, y, "     ", ha="center", va="center", fontsize=10, color="black", weight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor=color, lw=1, alpha=0.7))

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
