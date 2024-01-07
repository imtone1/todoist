import csv

#read csv file and return list of tasks
def read_tasks_from_csv(file_path):
    """
    Reads tasks from a CSV file and returns a list of tasks.

    Parameters:
        - file_path (str): The path to the CSV file.

    Returns:
        list: A list of tasks.
    """
    try:
        tasks = []
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(row)
        return tasks
    except Exception as error:
        print(error)
        return None
    
#open csv file and substitude content of child_tasks column to "content" column
def create_subtasks(tasks, main_task, due_date):
    """
    Creates subtasks from a list of tasks.

    Parameters:
        - tasks (list): A list of tasks.

    Returns:
        list: A list of subtasks.
    """
    try:
        subtasks = []
        for task in tasks:
            subtask = task.copy()
            subtask['due_date'] = due_date
            subtask['child_tasks'] = main_task
            subtasks.append(subtask)
        return subtasks
    except Exception as error:
        print(error)
        return None
    

class Task:
    def __init__(self, content, description, order, priority, project_id, labels, due_date, section_id, parent_id, child_tasks):
        self.content = content
        self.description = description
        self.order = order
        self.priority = priority
        self.project_id = project_id
        self.labels = labels
        self.due_date = due_date
        self.section_id = section_id
        self.parent_id = parent_id
        self.child_tasks = child_tasks

def open_csv_file(file_path, task):
        
    with open(file_path, "r",encoding='utf-8') as op:
        dt = csv.DictReader(op) 
        print(dt) 
        up_dt = [] 
        for r in dt: 
            print(r) 
            row = {'content': r['content'], 
                'description': r['description'], 
                'order': r['order'], 
                'priority': task.priority,
                'project_id': r['project_id'],
                'labels': r['labels'],
                'due_date': task.due_date,
                'section_id': r['section_id'],
                'parent_id': r['parent_id'],
                'child_tasks': task.content
                } 
            up_dt.append(row) 
        print(up_dt) 


#read csv file and make Task objects
def read_tasks_from_csv(file_path):
    """
    Reads tasks from a CSV file and returns a list of Task items.

    Parameters:
        - file_path (str): The path to the CSV file.

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
                parent_id=row['parent_id'] if row['parent_id'] else None,
                child_tasks=row['child_tasks'] if row['child_tasks'] else None
                )
            tasks.append(task)
    return tasks

#write Task objects to csv file
def write_tasks_to_csv(file_path, tasks):
    """
    Writes tasks to a CSV file.

    Parameters:
        - file_path (str): The path to the CSV file.
        - tasks (list): A list of Task objects.

    Returns:
        None
    """
    with open(file_path, 'w', newline='', encoding='utf-8' ) as file:
        writer = csv.writer(file)
        writer.writerow(["content", "description", "order", "priority", "project_id", "labels", "due_date", "section_id", "parent_id", "child_tasks"])
        #writer.writerows(tasks)
        for task in tasks:
            writer.writerow([task.content, task.description, task.order, task.priority, task.project_id, task.labels, task.due_date, task.section_id, task.parent_id, task.child_tasks])

tasks=read_tasks_from_csv('./todoist_api/todoist_api_app/tasks_data.csv')
subtasks=read_tasks_from_csv('./todoist_api/todoist_api_app/subtasks_data.csv')