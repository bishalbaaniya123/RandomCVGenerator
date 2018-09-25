import random


def return_education_section():
    colleges = ['Virginia Military Institute',
                'University of California, Santa Barbara',
                'Georgetown University',
                'Pepperdine University',
                'United States Coast Guard Academy',
                'Brigham Young University',
                'Centre College',
                'Vassar College',
                'Macalester College',
                'Scripps College'
                ]

    start_date = random.choice([2011, 2012, 2013, 2014, 2015, 2016])
    end_date = start_date + 4
    final_json = {
        "college": random.choice(colleges),
        "dateStart": start_date,
        "level": "Other",
        "university": "Trinity International Higher Secondary School & College",
        "degree": "Higher Secondary, Science",
        "location": "Kathmandu",
        "dateEnd": end_date
    }
    return final_json
