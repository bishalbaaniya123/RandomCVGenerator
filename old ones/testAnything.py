string = 'softSkillsInMyHead'
for i, c in enumerate(string):
    if c.isupper():
        string = string.replace(c, " " + c)
string = string.title()