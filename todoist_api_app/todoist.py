from todoist_api_python.api import TodoistAPI
    #muuttujat
from muuttujat import *

api_key = TodoistAPI(TODOIST_API_KEY)

class Task:
    def __init__(self, content=None, description=None, order=1, priority=1, project_id=None, labels=[], due_date=None, section_id=None, parent_id=None, due_lang="fi"):
        self.content = content
        self.description = description
        self.order = order
        self.priority = priority
        self.project_id = project_id
        self.labels = labels
        self.due_date = due_date
        self.section_id = section_id
        self.parent_id = parent_id
        self.due_lang=due_lang

######################################################################################################## API related functions
def get_all_projects(api_key):
    """Gets all projects. Returnes a list of Project items."""

    try:
        projects = api_key.get_projects()
        return projects
        
    except Exception as error:
        print(error)

def get_one_project(api_key, project_id):
    """Gets project object related to the given ID."""
    try:
        project = api_key.get_project(project_id=project_id)
        #print(project)
        return project
    except Exception as error:
        print(error)
        return None
    
def add_new_task(api_key, task):
    """Adds a new task to given project. Returnes a Task item."""

    try:
        added_task = api_key.add_task(
            content=task.content,
            description=task.description,
            order=task.order,
            priority=task.priority,
            project_id=task.project_id,
            labels=task.labels,
            due_date=task.due_date,
            section_id=task.section_id,
            parent_id=task.parent_id
        )
        print(f"Added task: {added_task}")
    except Exception as error:
        print(error)

######################################################################################################## Helper functions
def find_project(projects, project_name):
    """Finds a project by name. Returnes a project id."""
    try:
        for project in projects:
            if project.name == project_name:
                print(f"Found project: {project}")
            #print(project)
                return project.id
        return None
    except Exception as error:
        print(error)
        return None      

def main():
    
    projects=get_all_projects(api_key)
    project_id = find_project(projects, "Inbox")
    task = Task(
        content="labels",
        description="dekaögsd",
        order=1,
        priority=1,
        project_id=project_id,
        labels=["label1", "Python"],
        due_date="2024-01-06"
        )
  
    add_new_task(api_key, task)

if __name__ == "__main__":
    main()