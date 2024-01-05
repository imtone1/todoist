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

| Function Name          | Description                                                         | Parameters                           | Returns                                        |
|------------------------|---------------------------------------------------------------------|--------------------------------------|------------------------------------------------|
| `get_all_projects`     | Retrieves all projects from Todoist.                                | `api_key`                            | List of Project objects                        |
| `get_one_project`      | Fetches a specific project by its ID.                               | `api_key`, `project_id`              | Project object or `None`                       |
| `get_all_sections`     | Retrieves all sections within a specified project.                  | `api_key`, `project_id`              | List of Section objects or `None`              |
| `add_new_task`         | Adds a new task to a project.                                       | `api_key`, `task`                    | Print added Task object or error message       |
| `find_item_id`         | Finds an item (like a project or section) by name and returns its ID. | `items`, `item_name`               | Item ID or `None`                              |
| `read_tasks_from_csv`  | Reads tasks from a CSV file and returns a list of Task objects.     | `file_path`                          | List of Task objects                           |


# Dependences:

- Python
- [Poetry](https://python-poetry.org/docs/)