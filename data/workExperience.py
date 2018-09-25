import random


def return_work_experience():
    location = ['66 North Queen Ave. Park Forest, IL 60466',
                '104 Creekside St. Brooklyn, NY 11201',
                '32 Victoria Ave. Meadville, PA 16335',
                '74 Hickory Road Perth Amboy, NJ 08861',
                '7685 Hanover Ave. Methuen, MA 01844',
                '299 S. Birchpond Dr. Upper Darby, PA 19082',
                '8357 Tarkiln Hill St. Minneapolis, MN 55406',
                '637 Glen Creek Ave. Hyde Park, MA 02136',
                '8314 Sugar Ave. Greensburg, PA 15601',
                '19 Branch Street West Babylon, NY 11704']
    job_titles = [
        'Able Seamen Jobs',
        'Account Manager',
        'Accountant Jobs',
        'Actor Jobs',
        'Actuary Jobs',
        'Adjustment Clerk Jobs',
        'Admin Jobs',
        'Administrative Law Judge Jobs',
        'Administrative Services Manager Jobs',
        'Administrative Support Supervisors Jobs',
        'Advertising Manager',
        'Promotions Manager Jobs'
    ]
    organization = ['Morgan Stanley',
                    '3M',
                    'Cartier SA',
                    'Home Depot',
                    'Nintendo',
                    'Google',
                    'Hewlett-Packard',
                    'Prada',
                    'MTV',
                    'BlackBerry']
    months = ['January',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December']
    start_year = random.randint(2000, 2018)
    start_date = random.choice(months) + " " + str(start_year)
    if start_year <= 2014:
        end_date = random.choice(months) + " " + str(start_year + 4)
    else:
        end_date = "Present"

    level = random.choice(["Bachelors", "Masters", "Doctoral"])

    final_json = {
        "skills": {
            "softSkills": [],
            "database": [
                "MONGO"
            ],
            "framework": [
                "SPRING",
                "JWT"
            ],
            "webTechnologies": [],
            "programmingLanguage": [
                "JAVA"
            ],
            "softwareTools": [],
            "dataScientistSkill": [],
            "operatingSystem": [],
            "finance": [
                "LOGIC"
            ]
        },
        "dateStart": start_date,
        "organization": random.choice(organization),
        "jobTitle": random.choice(job_titles),
        "location": random.choice(location),
        "dateEnd": end_date
    }
    # print("\nlocation: " + final_json['location'])
    return final_json


return_work_experience()
