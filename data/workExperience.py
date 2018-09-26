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
    soft_skills = ['COMMUNICATION',
                   'TEAMWORK',
                   'ADAPTABILITY',
                   'PROBLEM-SOLVING',
                   'CREATIVITY',
                   'WORK ETHIC',
                   'INTERPERSONAL SKILLS',
                   'TIME MANAGEMENT',
                   'LEADERSHIP',
                   'ATTENTION TO DETAIL']
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
                  'ANGULARJS',
                  'RUBY ON RAILS',
                  'ASP.NET MVC',
                  'REACT',
                  'DJANGO',
                  'ANGULAR',
                  'LARAVEL',
                  'SPRING',
                  'VUE.JS',
                  'EXPRESS',
                  'METEOR',
                  'SYMFONY',
                  'FLASK',
                  'CODEIGNITER',
                  'EMBER.JS']
    frameworks_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(frameworks)
        if item not in frameworks_array:
            frameworks_array.append(item)

    web_technologies = ['DRAMATIC WEB LANGUAGES',
                        'CMS/E-COMMERCE',
                        'SEO/WEB STANDARDS',
                        'WEB SECURITY',
                        'DESIGN CONCEPTS',
                        'VERSION CONTROL',
                        'AGILE PROGRAMMING',
                        'PROJECT MANAGEMENT',
                        'PROJECT METHODOLOGIES',
                        'FRAMEWORKS',
                        'KNOWLEDGE RESOURCES',
                        'CLOUD TECHNOLOGIES',
                        'OPERATING SYSTEMS']
    web_technologies_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(web_technologies)
        if item not in web_technologies_array:
            web_technologies_array.append(item)

    programming_languages = ['JAVASCRIPT',
                             'JAVA',
                             'PYTHON',
                             'PHP',
                             'RUBY',
                             'SWIFT',
                             'C#',
                             'C++',
                             'JAVA',
                             'C']
    programming_languages_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(programming_languages)
        if item not in programming_languages_array:
            programming_languages_array.append(item)

    software_tools = ['NETBEANS',
                      'CLOUD9 IDE',
                      'ZEND STUDIO',
                      'ATOM',
                      'SPIRALOGICS APPLICATION ARCHITECTURE',
                      'CODELOBSTER',
                      'CODECHARGE STUDIO',
                      'BOOTSTRAP',
                      'EXPRESSION STUDIO',
                      'HTML5 BUILDER']
    software_tools_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(software_tools)
        if item not in software_tools_array:
            software_tools_array.append(item)

    data_scientists_skills = ['APPENGINE',
                              'ASSERTIVENESS',
                              'AWS',
                              'BIG DATA',
                              'C++',
                              'COLLABORATION',
                              'COMMUNICATION',
                              'COMPUTER SKILLS',
                              'CONSTRUCTING PREDICTIVE MODELS',
                              'CONSULTING',
                              'CONVEYING TECHNICAL INFORMATION TO NON-TECHNICAL PEOPLE',
                              'COUCHDB',
                              'CREATING ALGORITHMS',
                              'CREATING CONTROLS TO ASSURE ACCURACY OF DATA']
    data_scientists_skills_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(data_scientists_skills)
        if item not in data_scientists_skills_array:
            data_scientists_skills_array.append(item)

    operating_systems = ['MAC OS X',
                         'UNIX',
                         'UBUNTU',
                         'BEOS',
                         'IRIX',
                         'NEXTSTEP',
                         'MS-DOS',
                         'WINDOWS',
                         'IOS',
                         'CENTOS']
    operating_systems_array = []
    for _ in range(random.randint(0, 4)):
        item = random.choice(operating_systems)
        if item not in operating_systems_array:
            operating_systems_array.append(item)

    financial_skills = ['A FORMAL ACCOUNTING QUALIFICATION',
                        'INTERPERSONAL SKILLS',
                        'ABILITY TO COMMUNICATE',
                        'REPORTING',
                        'ANALYTICAL ABILITY',
                        'PROBLEM SOLVING SKILLS',
                        'KNOWLEDGE OF IT SOFTWARE',
                        'MANAGEMENT EXPERIENCE',
                        'COMMERCIAL ACUMEN',
                        'CAPACITY FOR INNOVATION']
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
    # for key, value in final_json['skills'].items():
    #     # print("key", key, " value: ", value)
    #     for item in value:
    #         print(item)
    #     print("\n")
    # print("\nfinancial_skills_array : ", final_json['skills']['finance'])
    return final_json


return_work_experience()
