from todoist_api_python.api import TodoistAPI
    #muuttujat
from muuttujat import *

api_key = TodoistAPI(TODOIST_API_KEY)

def get_my_projects(api_key):
    """Gets all projects. Returnes a list of Project items."""

    try:
        projects = api_key.get_projects()
        for project in projects:
            print(project)
        
    except Exception as error:
        print(error)

def get_one_project(api_key, project_id):
    """Gets project object related to the given ID. A successful response has 200 OK status and application/json Content-Type."""
    try:
        project = api_key.get_project(project_id=project_id)
        #print(project)
        return project.id
    except Exception as error:
        #print(error)
        return None

def add_new_task(api_key, project_id):
    """Adds a new task to given project. Returnes a Task item."""

    try:
        task = api_key.add_task(content="Buy Milk", project_id=project_id)
        print(task)
    except Exception as error:
        print(error)

def main():
    get_my_projects(api_key)
    get_one_project(api_key,"1534016461")

if __name__ == "__main__":
    main()