import random
import csv
from todoist_api_app.classes import *
from datetime import datetime, timedelta

from collections import defaultdict


def random_data():
    
    labels = ["Lean menetelmät", "Luova ongelmaratkaisu", "Gigitaalitekniikka", "Algoritmit", "Olio-ohjelmointi", "Projektit liiketoimintana", "Projektisalkun johtaminen"]
    sections = ["Projektijohtaminen", "Jamk"]

    with open('./todoist_api/todoist_api_app/tasks_data.csv', 'w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["content", "description", "order", "priority", "project_id", "labels", "due_date", "section_id", "parent_id", "child_tasks"])

        for i in range(20):
            content = f"task{i+1}"
            description = f"description for task{i+1}"
            order = i+1
            priority = random.randint(1, 4)
            project_id = "Inbox"
            task_labels = random.choice(labels)
            due_date = "2024-01-07"
            section_id = random.choice(sections)
            parent_id = ""
            child_tasks = ""

            writer.writerow([content, description, order, priority, project_id, task_labels, due_date, section_id, parent_id, child_tasks])


def issue_to_task(task, label, section, project, order_num=1, priority_num=1):
    task_object = Task(
        content = task.title,
        description = task.description,
        order = order_num,
        priority = priority_num,
        project_id = project,
        labels = label,
        due_date = task.due_date,
        section_id = section,
        parent_id = "",
        child_tasks = ""
        )
    return task_object

def task_to_csv(file_path:str, task_objects:list):
   
    with open(file_path, 'w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["content", "description", "order", "priority", "project_id", "labels", "due_date", "section_id", "parent_id", "child_tasks"])

        for task_object in task_objects:
            
            writer.writerow([task_object.content, task_object.description, task_object.order, task_object.priority, task_object.project_id, task_object.labels, task_object.due_date, task_object.section_id, task_object.parent_id, task_object.child_tasks])

def read_issue_from_csv(file_path:str):
    """
    Reads tasks from a CSV file and returns a list of Task items. Task is in form as imported from gitlab issues. Headers title, description, due_date.

    Parameters:
        - file_path (str): The path to the CSV file.

    Returns:
        list: A list of Task objects.

    """
    tasks = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            task = Issue(
            title=row['title'] if row['title'] else None,
            description=row['description'] if row['description'] else None,
            due_date=row['due_date'] if row['due_date'] else None
            )
            tasks.append(task)
            
    return tasks

def group_tasks_by_due_date(tasks):
    grouped_tasks = defaultdict(list)
    for task in tasks:
        grouped_tasks[task.due_date].append(task)
    return grouped_tasks

def count_items_in_groups(grouped_tasks):
    counts = {}
    for due_date, tasks in grouped_tasks.items():
        counts[due_date] = len(tasks)
    return counts


def sundays_between_dates(start_date, end_date):
    """
    Calculate the dates of Sundays between two dates.
    """
    
    sunday_dates = []

    # Calculate the number of days until the first Sunday from start_date
    days_until_next_sunday = (6 - start_date.weekday()) % 7
    current_date = start_date + timedelta(days=days_until_next_sunday)

    # Loop through, adding each Sunday to the list
    while current_date <= end_date:
        sunday_dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(weeks=1)

    return sunday_dates


from datetime import datetime, timedelta

def distribute_tasks_evenly(tasks, initial_due_date, max_tasks_per_date=4):
    """
    Distribute tasks evenly across weeks, starting from the initial due date, 
    so that there are no more than max_tasks_per_date tasks on the same date.

    Return: Dictionary with tasks as keys and their new due dates as values.
    """
    # Calculate the total number of weeks needed
    total_weeks_needed = -(-len(tasks) // max_tasks_per_date)  # Ceiling division

    # Assign new due dates to tasks
    task_due_dates = {}
    current_date = initial_due_date
    for i, task in enumerate(tasks):
        if i % max_tasks_per_date == 0 and i != 0:
            # Move to the next week when max_tasks_per_date is reached
            current_date += timedelta(weeks=1)
        task_due_dates[task] = current_date.strftime("%Y-%m-%d")

    return task_due_dates


def redistribute_tasks(tasks, max_tasks_per_date=2):
    """
    Redistribute tasks evenly across weeks, starting from their initial due dates, 
    so that there are no more than max_tasks_per_date tasks on the same date.

    Return: List of Task objects with updated due dates.
    """
    # Group tasks by due date
    grouped_tasks = group_tasks_by_due_date(tasks)

    # Redistribute tasks
    for due_date, tasks_on_date in grouped_tasks.items():
        if len(tasks_on_date) > max_tasks_per_date:
            current_date = datetime.strptime(due_date, "%Y-%m-%d")
            for i, task in enumerate(tasks_on_date):
                if i % max_tasks_per_date == 0 and i != 0:
                    # Move to the next week when max_tasks_per_date is reached
                    current_date += timedelta(weeks=1)
                task.due_date = current_date.strftime("%Y-%m-%d")

    return tasks

def main():

    issues=read_issue_from_csv('./todoist_api/todoist_api_app/data/issues_argorithm.csv')
    project="Inbox"
    section="Jamk"
    course="Data structures and algorithms"
    order_num=0
    priority=2
    tasks=[]
    for issue in issues:
        order_num+=1
        task=issue_to_task(issue, course, section, project, order_num, priority)
        tasks.append(task)

    # sundays between dates
    start = datetime(2024, 1, 8)
    end = datetime(2024, 2, 22)
    sundays=sundays_between_dates(start, end)
    
    print(sundays)
    task_to_csv('./todoist_api/todoist_api_app/data/tasks_algorithm.csv', tasks)
    # group_tasks_by_due_date(tasks)
    # for task in tasks:
    #     print(task.content, task.due_date)
    # grouped_tasks = group_tasks_by_due_date(tasks) 
    # counts = count_items_in_groups(grouped_tasks)
    # print(f"Counts: {counts}")

    # # Redistribute tasks
    # redistributed_tasks = redistribute_tasks(tasks, max_tasks_per_date=3)
    # for task in redistributed_tasks:
    #     print(task.content, task.due_date)

    # with open('./todoist_api/todoist_api_app/data/wuip_exercises.csv', newline='', encoding='utf-8') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     first_row = next(reader)
    #     print(first_row.keys())

if __name__ == "__main__":
    main()