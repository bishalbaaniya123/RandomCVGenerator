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
    universities = ['Cornell University',
                    'Georgia Institute of Technology',
                    'Lehigh University',
                    'Brown University',
                    'Georgetown University',
                    'University of Pennsylvania',
                    'DePauw University',
                    'Wheaton College',
                    'United States Coast Guard Academy',
                    'Pennsylvania State University, University Park'
                    ]
    degree = ['Associate Degree in Administration of Justice',
              'Associate Degree in Advertising',
              'Associate Degree in Agribusiness',
              'Associate Degree in Animal Management',
              'Associate Degree in Architectural Building Engineering Technology',
              'Associate Degree in Architecture and Career Options',
              'Associate Degree in Art',
              'Associate Degree in Automotive Maintenance Technology',
              'Associate Degree in Aviation Mechanics',
              'Associate Degree in Behavioral Science',
              'Associate Degree in Boat Mechanics',
              'Associate Degree in Boat Repair and Maintenance',
              'Associate Degree in Cabinet Design Technology',
              'Associate Degree in Child Development: Program Summary',
              'Associate Degree in Christian Ministry',
              'Associate Degree in Cosmetology Business',
              'Associate Degree in Digital Media',
              'Associate Degree in Early Childhood Special Education',
              'Associate Degree in Elementary Education']
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
    start_date = random.randint(2000, 2018)
    if start_date <= 2014:
        end_date = str(start_date + 4)
    else:
        end_date = ""

    level = random.choice(["Bachelors", "Masters", "Doctoral"])

    final_json = {
        "college": random.choice(colleges),
        "dateStart": str(start_date),
        "level": level,
        "university": random.choice(universities),
        "degree": random.choice(degree),
        "location": random.choice(location),
        "dateEnd": end_date
    }
    return final_json
