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

    # skills
    soft_skills = ['Communication',
                   'Teamwork',
                   'Adaptability',
                   'Problem-Solving',
                   'Creativity',
                   'Work Ethic',
                   'Interpersonal Skills',
                   'Time Management',
                   'Leadership',
                   'Attention to Detail']
    soft_skills_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(soft_skills)
        if item not in soft_skills_array:
            soft_skills_array.append(item)

    databases = ['DB2',
                 'MYSQL',
                 'ORACLE',
                 'POSTGRESQL',
                 'SQLITE',
                 'SQL SERVER',
                 'SYBASE',
                 'RETHINKDB',
                 'BERKELEY DB',
                 'MEMCACHED',
                 'REDIS',
                 'COUCHDB',
                 'MONGODB'
                 ]
    database_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(databases)
        if item not in database_array:
            database_array.append(item)

    frameworks = ['ASP.NET',
                  'AngularJS',
                  'Ruby on Rails',
                  'ASP.NET MVC',
                  'React',
                  'Django',
                  'Angular',
                  'Laravel',
                  'Spring',
                  'Vue.js',
                  'Express',
                  'Meteor',
                  'Symfony',
                  'Flask',
                  'CodeIgniter',
                  'Ember.js']
    frameworks_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(frameworks)
        if item not in frameworks_array:
            frameworks_array.append(item)

    web_technologies = ['Dramatic Web Languages',
                        'CMS/E-Commerce',
                        'SEO/Web Standards',
                        'Web Security',
                        'Design Concepts',
                        'Version Control',
                        'Agile Programming',
                        'Project Management',
                        'Project Methodologies',
                        'Frameworks',
                        'Knowledge Resources',
                        'Cloud Technologies',
                        'Operating Systems']
    web_technologies_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(web_technologies)
        if item not in web_technologies_array:
            web_technologies_array.append(item)

    programming_languages = ['JavaScript',
                             'Java',
                             'Python',
                             'PHP',
                             'Ruby',
                             'Swift',
                             'C#',
                             'C++',
                             'Java',
                             'C']
    programming_languages_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(programming_languages)
        if item not in programming_languages_array:
            programming_languages_array.append(item)

    software_tools = ['NetBeans',
                      'Cloud9 IDE',
                      'Zend Studio',
                      'Atom',
                      'Spiralogics Application Architecture',
                      'CodeLobster',
                      'CodeCharge Studio',
                      'Bootstrap',
                      'Expression Studio',
                      'HTML5 Builder']
    software_tools_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(software_tools)
        if item not in software_tools_array:
            software_tools_array.append(item)

    data_scientists_skills = ['AppEngine',
                              'Assertiveness',
                              'AWS',
                              'Big Data',
                              'C++',
                              'Collaboration',
                              'Communication',
                              'Computer Skills',
                              'Constructing Predictive Models',
                              'Consulting',
                              'Conveying Technical Information to Non-Technical People',
                              'CouchDB',
                              'Creating Algorithms',
                              'Creating Controls to Assure Accuracy of Data', ]
    data_scientists_skills_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(data_scientists_skills)
        if item not in data_scientists_skills_array:
            data_scientists_skills_array.append(item)

    operating_systems = ['Mac OS X',
                         'Unix',
                         'Ubuntu',
                         'BeOS',
                         'IRIX',
                         'NeXTSTEP',
                         'MS-DOS',
                         'Windows',
                         'iOS',
                         'CentOS']
    operating_systems_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(operating_systems)
        if item not in operating_systems_array:
            operating_systems_array.append(item)

    financial_skills = ['A formal accounting qualification',
                        'Interpersonal skills',
                        'Ability to communicate',
                        'Reporting',
                        'Analytical ability',
                        'Problem Solving skills',
                        'Knowledge of IT software',
                        'Management experience',
                        'Commercial acumen',
                        'Capacity for innovation']
    financial_skills_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(financial_skills)
        if item not in financial_skills_array:
            financial_skills_array.append(item)

    start_year = random.randint(2000, 2018)
    start_date = random.choice(months) + " " + str(start_year)
    if start_year <= 2014:
        end_date = random.choice(months) + " " + str(start_year + 4)
    else:
        end_date = "Present"

    level = random.choice(["Bachelors", "Masters", "Doctoral"])

    final_json = {
        "skills": {
            "softSkills": soft_skills_array,
            "database": database_array,
            "framework": frameworks_array,
            "webTechnologies": web_technologies_array,
            "programmingLanguage": programming_languages_array,
            "softwareTools": software_tools_array,
            "dataScientistSkill": data_scientists_skills_array,
            "operatingSystem": operating_systems_array,
            "finance": financial_skills_array
        },
        "dateStart": start_date,
        "organization": random.choice(organization),
        "jobTitle": random.choice(job_titles),
        "location": random.choice(location),
        "dateEnd": end_date
    }
    # print("\nfinancial_skills_array : ", final_json['skills']['finance'])
    return final_json


return_work_experience()
