from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Function to get item details from user
def get_item_details():
    date = input("Enter Date (DD/MM/YYYY): ")
    name = input("Enter Item Name: ")
    brand = input("Enter Brand: ")
    price = input("Enter Price (Rs.): ")
    return [date, name, brand, price]

# Main function to generate receipt
def generate_receipt():
    # Create an empty list to hold data
    DATA = [["Date", "Name", "Brand", "Price (Rs.)"]]
    
    # Get item details from the user
    while True:
        item_details = get_item_details()
        DATA.append(item_details)
        add_more = input("Do you want to add another item? (yes/no): ").lower()
        if add_more != 'yes':
            break
    
    # Calculate subtotal, discount, and total
    subtotal = sum(float(item[3].replace(',', '').replace('/-', '')) for item in DATA[1:])
    discount = 300.00 
    total = subtotal - discount
    
    # Add subtotal, discount, and total to the data
    DATA.append(["Sub Total", "", "", f"{subtotal:,.2f}/-"])
    DATA.append(["Discount", "", "", f"-{discount:,.2f}/-"])
    DATA.append(["Total", "", "", f"{total:,.2f}/-"])

    # Creating a Base Document Template of page size A4 
    pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4) 

    # Standard stylesheet defined within reportlab itself 
    styles = getSampleStyleSheet() 

    # Fetching the style of Top level heading (Heading1) 
    title_style = styles["Heading1"] 
    title_style.alignment = 1

    # Creating the paragraph with the heading text and passing the styles of it 
    title = Paragraph("Your Receipt", title_style) 

    # Creates a Table Style object and defines the styles row-wise 
    style = TableStyle([ 
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
    ]) 

    # Creating a table object and passing the style to it 
    table = Table(DATA, style=style) 

    pdf.build([title, table])

generate_receipt()
