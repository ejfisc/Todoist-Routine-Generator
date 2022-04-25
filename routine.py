#! python3
# routine.py - sends a list of tasks to my Todoist inbox every day

from todoist_api_python.api import TodoistAPI

# construct an instance of TodoistAPI using my user token for authentication
api = TodoistAPI('redacted for privacy purposes')

inbox = 0 # project_id of my inbox

# add routine tasks to inbox
try:
    make_bed = api.add_task(content='Make Bed', project_id=inbox, due_string='today')
    drink_water = api.add_task(content='Drink Water', project_id=inbox, due_string='today')
    internship_apps = api.add_task(content='Apply for Internships', project_id=inbox, due_string='today')
    dsa_practice = api.add_task(content='Study Data Structures & Algorithms', project_id=inbox, due_string='today')
    breakfast = api.add_task(content='Eat Breakfast', project_id=inbox, due_string='today')
    exercise = api.add_task(content='Exercise', project_id=inbox, due_string='today')
except Exception as error:
    print(error)