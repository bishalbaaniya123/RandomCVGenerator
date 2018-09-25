from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import random

c = canvas.Canvas("test001.pdf")
my_text = "Hello\nThis is a multiline text\nHere we do not have to handle the positioning of each line manually"

text_object = c.beginText(2 * cm, 29.7 * cm - 2 * cm)
for line in my_text.splitlines(False):
    text_object.textLine(line.rstrip())
c.drawText(text_object)
c.save()
