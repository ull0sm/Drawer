import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.image as mpimg

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


def draw_bracket(sheet_name, players, pdf, watermark_image):
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
    match_height = 1.85
    round_width = 4.0

    fig, ax = plt.subplots(figsize=(num_rounds * round_width, num_players * match_height / 2))
    ax.set_xlim(0, num_rounds * round_width)
    ax.set_ylim(0, num_players * match_height)
    ax.set_facecolor(bg_color)  # Set background color for the entire bracket
    ax.axis("off")

    positions = []

    # Load and display the watermark image
    watermark = mpimg.imread(watermark_image)  # Load the PNG image
    watermark_height, watermark_width, _ = watermark.shape  # Get original image dimensions
    aspect_ratio = watermark_width / watermark_height  # Calculate aspect ratio

    # Set watermark size to fit within the plot
    plot_width = num_rounds * round_width
    plot_height = num_players * match_height

    # Calculate new dimensions to maintain aspect ratio
    new_width = plot_width * 0.5  # Watermark width as 50% of plot width
    new_height = new_width / aspect_ratio  # Calculate height to maintain aspect ratio

    # Position the watermark image (adjust x, y for desired placement)
    ax.imshow(watermark, aspect='auto', extent=[(plot_width - new_width) / 2, (plot_width + new_width) / 2, 
                                                (plot_height - new_height) / 2, (plot_height + new_height) / 2],
              alpha=0.1)  # Adjust alpha for transparency

    # Draw the title with a modern font
    fig.suptitle(f"Shorin Kai Republic Bharat Cup", fontsize=18, weight='bold', y=0.92, color=text_color, family="sans-serif")
    
    # Additional sheet-specific text: sheet name and category
    fig.text(
        s=f"{sheet_name}",
        x=0.95, 
        y=0.98, 
        ha='right', 
        va='top',
        fontsize=12,       # Adjust font size
        color='black',  # Change text color
        backgroundcolor='lightyellow',  # Add a background color to the text
        family='sans-serif',    # Change the font family
        rotation=0,        # Optional: text rotation
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5') # Rounded box with padding
    )

    fig.text(
        s=f"Category:",
        x=0.05, 
        y=0.98, 
        ha='left', 
        va='top',
        fontsize=12,       # Adjust font size
        color='black',  # Change text color
        backgroundcolor='lightyellow',  # Add a background color to the text
        family='sans-serif',    # Change the font family
        rotation=0,        # Optional: text rotation
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5') # Rounded box with padding
    )

    # Draw initial round with alternating colors
    for i, player in enumerate(players):
        x = 0.75
        y = i * match_height
        color = blue if i % 2 == 0 else red  # Alternate colors with bold and visible red and blue
        # Split the player data into number/name and school
        parts = player.split("\n")
        if len(parts) == 1:
            name = parts[0]
            school = ""  # Assign "BYE" if no school part is provided
        else:
            name, school = parts

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

            x = round_idx * round_width * 0.80  # Increase x to make lines longer
            y = (current_positions[i][1] + current_positions[i + 1][1]) / 2

            # Draw connecting lines
            ax.plot([current_positions[i][0], x], [current_positions[i][1], y], color=color, lw=1)
            ax.plot([current_positions[i + 1][0], x], [current_positions[i + 1][1], y], color=color, lw=1)

            # Add placeholder for the winner
            ax.text(x, y, "", ha="center", va="center", fontsize=12, color=winner_color,
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor=winner_color, lw=1, alpha=0.4))

            # Add "Winner" box at each intersection
            ax.text(x, y, "     ", ha="center", va="center", fontsize=10, color="black", weight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor=color, lw=1, alpha=0.7))

            next_positions.append((x, y))

        current_positions = next_positions

    # Results Text
    results_text = """
    Results

    1st: _____________________________
           
    2nd: _____________________________
           
    3rd: _____________________________
           
    4th: _____________________________"""

    # Set text properties for better symmetry and spacing
    ax.text(0.9, 0.09, results_text, ha="center", va="center", fontsize=11, color="#333333", fontweight='bold',
        family='sans-serif', transform=ax.transAxes, linespacing=1.75)

    # Save the figure to the PDF
    pdf.savefig(fig)
    plt.close(fig)


def main():
    input_excel = "grouped_output.xlsx"  # Replace with your Excel file path
    output_pdf = "multi_page_tournament_bracket.pdf"
    watermark_image = "watermark.png"  # Replace with your watermark PNG file path

    # Read all sheets and their players
    sheet_players = read_excel_sheets(input_excel)

    # Open a PDF file for multi-page output
    with PdfPages(output_pdf) as pdf:
        for sheet_name, players in sheet_players.items():
            players = create_bracket(players)  # Ensure power of 2
            draw_bracket(sheet_name, players, pdf, watermark_image)

    print(f"Multi-page tournament bracket saved to {output_pdf}")


if __name__ == "__main__":
    main()
