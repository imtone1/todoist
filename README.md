# Todoist Task Adding Project

This project provides a Python script for adding tasks to your Todoist account.

# Prerequisites

- A [Todoist](https://todoist.com) account.
- An API token from Todoist. Read more about Todoist API documentation [here](https://developer.todoist.com/rest/v2#overview).

# Getting Started

To use this script, you need to change the values in muuttujat.txt to your own.

1. Add your Todoist API token to the muuttujat.txt file.

2. Rename muuttujat.txt to muuttujat.py. This changes the file into a Python module that can be used in the script.

## Activate the virtual environment

Activate the virtual environment with a nested shell provided by Poetry:

```powershell
poetry shell
```

To deactivate the virtual environment, type:

```powershell
exit
```

# Functions

| Function Name            | Description                                         | Parameters                                                    | Returns                                        |
|--------------------------|-----------------------------------------------------|---------------------------------------------------------------|------------------------------------------------|
| `get_all_projects`       | Retrieves all projects from Todoist.                | `api_key` (str): API key for authentication.                  | List of Project objects.                       |
| `get_one_project`        | Retrieves a specific project by its ID.             | `api_key` (str): API key.<br>`project_id` (int): ID of the project. | Project object or `None` if an error occurs.   |
| `get_all_sections`       | Retrieves all sections in a project.                | `api_key` (str): API key.<br>`project_id` (int): ID of the project. | List of Section objects or `None`.             |
| `add_new_task`           | Adds a new task to Todoist.                         | `api_key` (str): API key.<br>`task` (Task): Object containing task details. | Added Task object or `None`.                   |
| `find_item_id`           | Finds an item (e.g., project or section) by name and returns its ID. | `items` (list): List of items to search through.<br>`item_name` (str): Name of the item to find. | Item ID or `None` if not found.                |
| `read_tasks_from_csv`    | Reads tasks from a CSV file and returns a list of Task objects. | `file_path` (str): Path to the CSV file.                     | List of Task objects.                          |
| `check_if_str`           | Checks if the given `task_id` is a string.          | `task_id` (any): The `task_id` to check.                      | `True` if `task_id` is a string, otherwise `False`. |



# Dependences:

- Python
- [Poetry](https://python-poetry.org/docs/)