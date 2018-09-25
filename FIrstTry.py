import json
from pprint import pprint
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import random

cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('.\\cv_json\\aaronGibson.json', cur_path)

with open(new_path) as f:
    data = json.load(f)

pprint(data['candidateDetail']['name']['firstName'])

# actual reportlab code
c = canvas.Canvas("test" + str(random.randint(1, 1000)) + ".pdf")
final_string_to_be_rendered = "FirstName: " + data['candidateDetail']['name']['firstName'] + \
                              "\nMiddleName: " + data['candidateDetail']['name']['middleName'] + \
                              "\nLastName: " + data['candidateDetail']['name']['surname']

text_object = c.beginText(2 * cm, 29.7 * cm - 2 * cm)
for line in final_string_to_be_rendered.splitlines(False):
    text_object.textLine(line.rstrip())
c.drawText(text_object)
c.save()
