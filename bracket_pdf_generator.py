import pandas as pd
import random
from reportlab.pdfgen import canvas
from PIL import Image
import os
from PyPDF2 import PdfMerger
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

category = ""
SEX = 0

def read(filepath):
    # Create the temp folder if it doesn't exist, or clean it if it does
    output_folder = ".\\temp"
    if os.path.exists(output_folder):
        # Delete all files in the temp folder
        for filename in os.listdir(output_folder):
            file_path = os.path.join(output_folder, filename)
            os.unlink(file_path)
    else:
        # Create the temp folder if it doesn't exist
        os.makedirs(output_folder)
    
    # Read all sheets into a dictionary of DataFrames
    sheets = pd.read_excel(filepath, sheet_name=None)
    
    ctr = 0
    for sheet_name, df in sheets.items():
        text = []
        # Iterate through each row and create the formatted string for each row
        players = []
        for index, row in df.iterrows():
            temp = f"{row['Number']} | {row['Name']}"
            text.append(temp)
            players.extend([f"{row['Number']}", f"{row['Name']}", f"{row['School']}"])

        while len(text) < 8:
            text.append("BYE")
    
        random.shuffle(text)
        shuffle_limit = 10  # You can set this to any value you prefer
        shuffle_count = 0
        while shuffle_count < shuffle_limit:
            # Shuffle the list
            random.shuffle(text)
            
            # Check if 'BYE' is in an even index position
            if any(text[i] == 'BYE' for i in range(0, len(text), 2)):
                shuffle_count += 1  # Increment the shuffle count
                continue  # If 'BYE' is in even positions, shuffle again
            else:
                break  # If 'BYE' is not in even positions, stop shuffling
        create_bracket(text=text, ctr=ctr, players=players)
        ctr += 1 

def create_bracket(text, ctr, players):
    image_path = "score_sheet.png"  # Replace with your image file
    output_pdf_path = f".\\temp\\output_{ctr}.pdf"

    # Open the image to get its dimensions
    image = Image.open(image_path)
    width, height = image.size

    # Create a PDF canvas
    c = canvas.Canvas(output_pdf_path, pagesize=(width, height + 100))  # Add space for text
    
    # Draw the image onto the PDF
    c.drawImage(image_path, 0, 100, width, height)  # Place image slightly below to leave space for text

    pdfmetrics.registerFont(TTFont('font', 'Allan-Bold.ttf'))
    c.setFont('font', 60)  # Use bold font for the title
    c.drawString(620, 1450, "Shorin Kai Republic Bharat Cup - 2025")
    
    y = [1335, 1180, 1035, 880, 740, 580, 440, 280]
    for i in range(8):
        c.setFont("Helvetica-Bold", 30)  # Set font and size
        c.setFillAlpha(1.0)
        if(text[i]== "BYE"):
            c.setFont("Helvetica", 30)  # Set font and size
            c.setFillAlpha(0.35)  
        c.drawString(160, y[i], text=text[i])  # Position and content of the text
        
    c.setFillAlpha(1.0)
    c.rect(150, 1435, 110, 50)  # x, y, width, height
    c.setFont("Helvetica", 30)  # Set font and size
    c.drawString(160, 1450, text=f"Pool_{ctr+1}")
    
    c.setFont("Helvetica-Bold", 30)  # Set font and size
    c.drawString(SEX, 1370, "XXXX")  # Define which category
    c.setFont("Helvetica-Bold", 25)  # Set font and size
    c.drawString(1600, 1313, text=category)
    
    # New page
    c.showPage()
    c.setFont("font", 60)  # Use bold font for the title
    c.drawString(620, 1450, "Shorin Kai Republic Bharat Cup - 2025")
    c.setFont("Helvetica", 30)  # Set font and size
    c.drawString(160, 1300, "Number")
    c.drawString(350, 1300, "Name")
    c.drawString(860, 1300, "School")
    c.rect(150, 1435, 110, 50)  # x, y, width, height
    c.drawString(160, 1450, text=f"Pool_{ctr+1}")
    
    c.setFont("Helvetica", 20)  # Set font and size
    c.drawString(1600, 1450, text=f"Category : {category}")
    
    c.setFont("Helvetica", 30)  # Set font and size
    ctr = 0
    for i in range(int(len(players) / 3)):
        for j in range(3):
            N = 350
            if j == 1:
                N = 200
            c.drawString(160 + (j * N), 1230 - (i * 80), players[ctr])
            ctr += 1
    
    c.save()
    print(f"PDF with text saved at {output_pdf_path}")

def pdf_merger():
    inputfolder = ".\\temp"
    output_PDF = f".\\score_sheets\\{category}.pdf"

    # Initialize a PdfMerger object
    merger = PdfMerger()

    # Loop through all files in the input folder
    for filename in os.listdir(inputfolder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(inputfolder, filename)
            merger.append(file_path)

    # Write the merged PDF to the temp location
    merger.write(output_PDF)
    merger.close()

    print(f"Merged PDF is saved at {output_PDF}")

    # After merging, delete the temp folder and its contents
    for filename in os.listdir(inputfolder):
        file_path = os.path.join(inputfolder, filename)
        os.unlink(file_path)
    print(f"temp folder cleaned.")