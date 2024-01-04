from todoist_api_python.api import TodoistAPI
#muuttujat
from muuttujat import *

api = TodoistAPI(TODOIST_API_KEY)

try:
    projects = api.get_projects()
    for project in projects:
        print(project)
    
except Exception as error:
    print(error)