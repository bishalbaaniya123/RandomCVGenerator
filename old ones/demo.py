from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image

import csv

data_file = 'data.csv'


def import_data(data_csv_file):
    with open(data_csv_file, newline='') as csvfile:
        attendee_data = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in attendee_data:
            last_name = row[0]
            first_name = row[1]
            course_name = row[2]
            # print("this are the ones printed", first_name, last_name, course_name)
            pdf_file_name = course_name + "_" + last_name + " " + first_name + ".pdf"
            generate_certificate(first_name, last_name, course_name, pdf_file_name)


def generate_certificate(first_name, last_name, course_name, pdf_file_name):
    attendee_name = first_name + " " + last_name
    c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))

    # header text
    c.setFont('Helvetica', 48, leading=None)
    c.drawCentredString(415, 500, 'Certificate of Completion')
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 450, 'This certificate is presented to ')
    # attendee
    c.setFont('Helvetica-Bold', 34, leading=None)
    c.drawCentredString(415, 395, attendee_name)
    # for completing the
    c.setFont('Helvetica', 24, leading=None)
    # c.drawCentredString(415, 450, 'for completing the following course:')
    # c.drawCentredString(415, 350, "")
    # course name
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(415, 310, course_name)
    # image seal
    seal = 'lannister_seal.jpg'
    c.drawImage(seal, 350, 50, width=None, height=None)
    # generate pdf
    c.showPage()

    c.save()


import_data(data_file)
