from reportlab.pdfgen import canvas
import random


def generate_pdf():
    string = "this is just a string <br />\n this should be on another line" + str(random.randint(1, 100))
    file_name = "sample" + str(random.randint(1, 100))
    print("this is the file_name", file_name)
    c = canvas.Canvas(file_name + ".pdf")
    c.setFont('Helvetica', 48, leading=None)
    c.drawCentredString(415, 500, string)
    c.save()

generate_pdf()