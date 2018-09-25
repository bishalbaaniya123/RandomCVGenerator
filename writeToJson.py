import json
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import random
# get data from files
from data.firstName import return_first_name
from data.jobTitle import return_job_titles
from data.lastName import return_last_name
from data.location import return_locations
from data.middleName import return_middle_name

# get some names
firstName = random.choice(return_first_name())
middleName = random.choice(return_middle_name())
lastName = random.choice(return_last_name())

jobTitle = random.choice(return_job_titles())
location = random.choice(return_locations())

# create json object
finalJson = {
    "candidateDetail": {
        "name": {
            "firstName": firstName,
            "middleName": middleName,
            "surname": lastName
        },
        "jobTitle": jobTitle,
        "address": location
    }
}

# generate the fileName
fileName = firstName + "_" + middleName + "_" + lastName + '.json'

# generate the json file and save it to the folder "Generated_Jsons"
with open(os.path.join('Generated_Jsons/', fileName), "w") as outfile:
    json.dump(finalJson, outfile)

'''
Use reportLab now to generate the pdf from the above generated json file and save pdf
'''
cur_path = os.path.dirname(__file__)

# get the path of the recently generated json file
path_for_json_file = os.path.relpath('.\\Generated_Jsons\\' + fileName, cur_path)

# open the file (generated file)
with open(path_for_json_file) as f:
    data = json.load(f)

# create a canvas object and later convert it to pdf
path_for_pdf_file = os.path.relpath('.\\Generated_Pdfs\\' + fileName, cur_path)
c = canvas.Canvas(path_for_pdf_file + ".pdf")

# generate the string
final_string_to_be_rendered = "FirstName: " + data['candidateDetail']['name']['firstName'] + \
                              "\nMiddleName: " + data['candidateDetail']['name']['middleName'] + \
                              "\nLastName: " + data['candidateDetail']['name']['surname']

# for line spacing
text_object = c.beginText(2 * cm, 29.7 * cm - 2 * cm)

# \n means nothing to reportLab unless this code executes
for line in final_string_to_be_rendered.splitlines(False):
    text_object.textLine(line.rstrip())

# render the text to the pdf file
c.drawText(text_object)

# save the pdf
c.save()