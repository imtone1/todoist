import random
import csv

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