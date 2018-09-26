import json
import os
import random

from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

# get data from files
from data.educationSection import return_education_section
from data.email import return_email
from data.firstName import return_first_name
from data.jobTitle import return_job_titles
from data.lastName import return_last_name
from data.location import return_locations
from data.middleName import return_middle_name
# get some names
from data.phone_number import return_phone_number
from data.skills import return_skills
from data.workExperience import return_work_experience
from reportlab.platypus import PageBreak

firstName = random.choice(return_first_name())
middleName = random.choice(return_middle_name())
lastName = random.choice(return_last_name())

jobTitle = random.choice(return_job_titles())
location = random.choice(return_locations())

phone_number_array = []
emails = []
education_section = []
work_experience = []
for _ in range(random.randint(0, 4)):
    item = random.choice(return_phone_number())
    if item not in phone_number_array:
        phone_number_array.append(item)

for _ in range(random.randint(0, 4)):
    item = random.choice(return_email())
    if item not in emails:
        emails.append(item)

for _ in range(random.randint(0, 4)):
    education_section.append(return_education_section())

for _ in range(random.randint(0, 4)):
    work_experience.append(return_work_experience())

# create json object
finalJson = {
    "candidateDetail": {
        "name": {
            "firstName": firstName,
            "middleName": middleName,
            "surname": lastName
        },
        "jobTitle": jobTitle,
        "address": location,
        "info": {
            "phone": phone_number_array,
            "email": emails
        },
        "educationSection": education_section,
        "workExperience": work_experience,
        "yearsOfExp": random.randint(1, 5),
        "skills": return_skills()
    }
}

# generate the fileName
fileName = firstName + "_" + middleName + "_" + lastName

# generate the json file and save it to the folder "Generated_Jsons"
with open(os.path.join('Generated_Jsons/', fileName + '.json'), "w") as outfile:
    json.dump(finalJson, outfile)

'''
Use reportLab now to generate the pdf from the above generated json file and save pdf
'''
cur_path = os.path.dirname(__file__)

# get the path of the recently generated json file
path_for_json_file = os.path.relpath('.\\Generated_Jsons\\' + fileName + ".json", cur_path)

# open the file (generated file)
with open(path_for_json_file) as f:
    data = json.load(f)

# create a canvas object and later convert it to pdf
path_for_pdf_file = os.path.relpath('.\\Generated_Pdfs\\' + fileName, cur_path)
c = canvas.Canvas(path_for_pdf_file + ".pdf")

# generate the string
final_string_to_be_rendered = "First Name: " + data['candidateDetail']['name']['firstName'] + \
                              "\nMiddle Name: " + data['candidateDetail']['name']['middleName'] + \
                              "\nLast Name: " + data['candidateDetail']['name']['surname'] + \
                              "\nJob Title: " + data['candidateDetail']['jobTitle'] + \
                              "\nAddress: " + data['candidateDetail']['address']

for idx, val in enumerate(data['candidateDetail']['info']['phone']):
    final_string_to_be_rendered += "\n\nPhone Number(" + str(idx + 1) + "): " \
                                   + data['candidateDetail']['info']['phone'][idx]
for idx, val in enumerate(data['candidateDetail']['info']['email']):
    final_string_to_be_rendered += "\n\ne-mail(" + str(idx + 1) + "): " \
                                   + data['candidateDetail']['info']['email'][idx]
for idx, val in enumerate(data['candidateDetail']['educationSection']):
    final_string_to_be_rendered += "\n\n\nEducation(" + str(idx + 1) + "): " \
                                   + "\nCollege: " + data['candidateDetail']['educationSection'][idx]['college'] \
                                   + "\nStart date: " + data['candidateDetail']['educationSection'][idx]['dateStart'] \
                                   + "\nLevel: " + data['candidateDetail']['educationSection'][idx]['level'] \
                                   + "\nUniversity: " + data['candidateDetail']['educationSection'][idx]['university'] \
                                   + "\nDegree: " + data['candidateDetail']['educationSection'][idx]['degree'] \
                                   + "\nLocation: " + data['candidateDetail']['educationSection'][idx]['location'] \
                                   + "\nEnd Date: " + data['candidateDetail']['educationSection'][idx]['dateEnd'] \
                                   + ""
for idx, val in enumerate(data['candidateDetail']['workExperience']):
    final_string_to_be_rendered += "\n\n\nWork Experience(" + str(idx + 1) + "): " \
                                   + "\nStart Date: " + data['candidateDetail']['workExperience'][idx]['dateStart'] \
                                   + "\nOrganization: " + data['candidateDetail']['workExperience'][idx]['organization'] \
                                   + "\nJob Title: " + data['candidateDetail']['workExperience'][idx]['jobTitle'] \
                                   + "\nLocation: " + data['candidateDetail']['workExperience'][idx]['location'] \
                                   + "\nEnd Date: " + data['candidateDetail']['workExperience'][idx]['dateEnd'] \
                                   + "\nSkills" \
                                   + ""
    for key, value in data['candidateDetail']['workExperience'][idx]['skills'].items():
        final_string_to_be_rendered += "\n\n" + key + ": "
        for itemValue in value:
            final_string_to_be_rendered += itemValue + "\n"

final_string_to_be_rendered += "\n\n\nSkills"
for key, value in data['candidateDetail']['skills'].items():
    final_string_to_be_rendered += "\n\n" + key + ": "
    for itemValue in value:
        final_string_to_be_rendered += itemValue + "\n"

# for line spacing
text_object = c.beginText(2 * cm, 29.7 * cm - 2 * cm)

# \n means nothing to reportLab unless this code executes
for line in final_string_to_be_rendered.splitlines(False):
    text_object.textLine(line.rstrip())

# render the text to the pdf file
c.drawText(text_object)

# save the pdf
c.save()
