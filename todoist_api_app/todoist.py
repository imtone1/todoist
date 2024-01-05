from todoist_api_python.api import TodoistAPI
    #muuttujat
from muuttujat import *
import csv

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
    """
    Gets all projects.

    Parameters:
        - api_key (str): The API key used for authentication.

    Returns:
        list of objects: A list of Project items.
    """

    try:
        projects = api_key.get_projects()
        return projects
        
    except Exception as error:
        print(error)

def get_one_project(api_key, project_id):
    """
    Gets project object related to the given ID.

    Parameters:
        - api_key (str): The API key used for authentication.
        - project_id (int): The ID of the project to retrieve.

    Returns:
    - object (Project): The project object related to the given ID, or None if an error occurs.
    """
    try:
        project = api_key.get_project(project_id=project_id)
        #print(project)
        return project
    except Exception as error:
        print(error)
        return None

def get_all_sections(api_key, project_id):
    """Gets all sections in a project. Returnes a json of Section items."""
    try:
        sections = api_key.get_sections(project_id=project_id)
        print(sections)
        return sections
    except Exception as error:
        print(error)
        return None
        
def add_new_task(api_key, task):
    """
    Add a new task to Todoist.

    Parameters:
        - api_key (str): The API key used for authentication.
        - task (Task): The task object containing the task details.

    Returns:
        Task: The added task object if successful, None otherwise.
    """

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
        return added_task
    except Exception as error:
        print(error)
        return None

######################################################################################################## Helper functions
def find_item_id(items, item_name):
    """
    Finds an item (e.g project or section) by name and returns its ID.

    Parameters:
        - items (list): A list of items to search through.
        - item_name (str): The name of the item to find.

    Returns:
        int or None: The ID of the found item, or None if not found.
    """
    try:
        for item in items:
            if item.name == item_name:
                print(f"Found item: {item}")
                return item.id
        return None
    except Exception as error:
        print(error)
        return None
    
def read_tasks_from_csv(file_path):
    """
    Reads tasks from a CSV file and returns a list of Task items.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of Task objects.

    """
    tasks = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            task = Task(
                content=row['content'] if row['content'] else None,
                description=row['description'] if row['description'] else None,
                order=int(row['order']) if row['order'] else 1,
                priority=int(row['priority']) if row['priority'] else 1,
                project_id=row['project_id'] if row['project_id'] else None,
                labels=row['labels'].split(',') if row['labels'] else [],
                due_date=row['due_date'] if row['due_date'] else None,
                section_id=row['section_id'] if row['section_id'] else None,
                parent_id=row['parent_id'] if row['parent_id'] else None
                )
            tasks.append(task)
    return tasks

def main():
    
    projects=get_all_projects(api_key)
    project_id = find_item_id(projects, "Inbox")

    get_all_sections(api_key, project_id)
    # task = Task(
    #     content="labels",
    #     description="dekaögsd",
    #     order=1,
    #     priority=1,
    #     project_id=project_id,
    #     labels=["label1", "Python"],
    #     due_date="2024-01-06"
    #     )
  
    # Adding tasks from csv file
    # tasks = read_tasks_from_csv('./todoist_api/todoist_api_app/task_data.csv')
    # print(tasks)
    # for task in tasks:
    #     add_new_task(api_key, task)

if __name__ == "__main__":
    main()