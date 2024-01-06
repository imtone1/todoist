import xml.etree.ElementTree as ET
from todoist_api_python.api import TodoistAPI
    #muuttujat
from muuttujat import *

api_key = TodoistAPI(TODOIST_API_KEY)

def get_all_active_tasks(api_key):
    """
    Retrieves all active tasks using the provided API key.

    Parameters:
    - api_key (str): The Todoist API key used for authentication.

    Returns:
    - list: A list of active tasks retrieved from the Todoist API or None if an error occurs.
    """
    try: 
        tasks = api_key.get_tasks()
        return tasks
    except Exception as error:
        print(error)
        return None


def add_task_to_xml(task, xml_file_path: str):
    """
    Adds a task to an XML file.

    Parameters:
        - task: The task object to be added.
        - xml_file_path: The path to the XML file.

    Returns:
        None
    """
    # XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    #Element where we will insert the new cell
    diagram = root.find(".//diagram/mxGraphModel/root")

    # mxCell element
    task_cell = ET.Element("mxCell")
    task_cell.set("id", task.id)
    task_cell.set("value", task.content)
    task_cell.set("style", "whiteSpace=wrap;rounded=1;shadow=1;fillColor=#10739E;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=24")
    task_cell.set("parent", "1")  # Assuming '1' is the common parent for cells
    task_cell.set("vertex", "1")

    # mxGeometry element
    geometry = ET.SubElement(task_cell, "mxGeometry")
    geometry.set("x", "220")  # Example position, can be modified
    geometry.set("y", "-10")  # Example position, can be modified
    geometry.set("width", "340")
    geometry.set("height", "60")
    geometry.set("as", "geometry")

    # Append the new cell to the diagram
    diagram.append(task_cell)

    # Write back to the file
    tree.write(xml_file_path)


def main():
    xml_file_path = './todoist_api/todoist_api_app/chart_copy.drawio'
    tasks=get_all_active_tasks(api_key)
    sorted_tasks = sorted(tasks, key=lambda task: task.due.date if task.due else "2040-00-00")


    # Group tasks by section_id and labels[0]
    tasks_by_section_and_label = {}
    for task in sorted_tasks:
        if task.section_id not in tasks_by_section_and_label:
            tasks_by_section_and_label[task.section_id] = {}
        if task.labels and task.labels[0] not in tasks_by_section_and_label[task.section_id]:
            tasks_by_section_and_label[task.section_id][task.labels[0]] = []
        if task.labels:
            tasks_by_section_and_label[task.section_id][task.labels[0]].append(task)
    print(f"Tasks by section and label {tasks_by_section_and_label}")
    for task in sorted_tasks:
        print(task)
        #add_task_to_xml(task, xml_file_path)
        print(f"Taso 1: {task.section_id}")
        #print(f"Taso 2: {task.labels[0]}")
        print(f"Taso 3: {task.content}")
    
    print(tasks[1].due.date)

    colors=["#ED9B09","#326CAD","#0974ED","#987639","#3B536E"]
    colors1=["#F007DA","#55B031","#4AF008","#9B3891","#4A703B"]

if __name__ == "__main__":
    main()