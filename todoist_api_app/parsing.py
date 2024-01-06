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

def get_all_sections(api_key, project_id):
    """
    Gets all sections in a project.

    Parameters:
        - api_key (str): The API key used for authentication.
        - project_id (int): The ID of the project.

    Returns:
    - sections (list): A list of Section items.
    """
    try:
        sections = api_key.get_sections(project_id=project_id)
        print(sections)
        return sections
    except Exception as error:
        print(error)
        return None

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

def find_item_name(items, item_id):
    """
    Finds an item (e.g project or section) by ID and returns its name.

    Parameters:
        - items (list): A list of items to search through.
        - item_id (int): The ID of the item to find.

    Returns:
        str or None: The name of the found item, or None if not found.
    """
    try:
        for item in items:
            if item.id == item_id:
                print(f"Found item: {item}")
                return item.name
        return None
    except Exception as error:
        print(error)
        return None

def add_task_to_xml(task_id:str, task_content:str, x_coodinate_course:int, y_coodinate:int, xml_file_path: str,fillcolor:str, fontstyle:int=0, fontsize:int=12,bordercolor: str="#000000",borderwidth:int=0):
    """
    Adds a task to an XML file.

    Parameters:
        - task_id (str): The ID of the task.
        - task_content (str): The content of the task.
        - x_coodinate_course (int): The x-coordinate of the task cell.
        - y_coodinate (int): The y-coordinate of the task cell.
        - xml_file_path (str): The path to the XML file.
        - fillcolor (str): The fill color of the task cell.
        - fontstyle (int, optional): The font style of the task cell. Defaults to 0.
        - fontsize (int, optional): The font size of the task cell. Defaults to 12.
        - bordercolor (str, optional): The border color of the task cell. Defaults to "#000000".
        - borderwidth (int, optional): The border width of the task cell. Defaults to 0.

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
    task_cell.set("id", task_id)
    task_cell.set("value", task_content)
    task_cell.set("style", f"whiteSpace=wrap;rounded=1;shadow=1;fillColor={fillcolor};strokeColor=none;fontColor=#FFFFFF;fontStyle={fontstyle};fontSize={fontsize};strokeWidth={borderwidth};strokeColor={bordercolor};")
    task_cell.set("parent", "1")
    task_cell.set("vertex", "1")

    # mxGeometry element
    geometry = ET.SubElement(task_cell, "mxGeometry")
    geometry.set("x", str(x_coodinate_course))
    geometry.set("y", str(y_coodinate))
    geometry.set("width", "120")
    geometry.set("height", "60")
    geometry.set("as", "geometry")

    # Append the new cell to the diagram
    diagram.append(task_cell)

    # Write back to the file
    tree.write(xml_file_path)


def main():
    xml_file_path = './todoist_api/todoist_api_app/chart_copy.drawio'
    projects=get_all_projects(api_key)
    tasks=get_all_active_tasks(api_key)
    project_id = find_item_id(projects, "Inbox")
    sections=get_all_sections(api_key, project_id)
    
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
    
    section_count=0
    task_count=1
    course_count=1
    between_sections=0
    colors=["#ED9B09","#326CAD","#0974ED","#987639","#3B536E"]
    colors1=["#F007DA","#55B031","#4AF008","#9B3891","#4A703B"]
    priority_colors=["#FFFFFF","#3cb371","#ffa500","#ff0000"]
    for section_id, labels in tasks_by_section_and_label.items():
        print(f"Section ID: {section_id}")
        section_count+=1
        section_name = find_item_name(sections, section_id)
        x_coodinate_section=-260+section_count*360
        
        for label, tasks in labels.items():
            
            print(f"Label: {label}")
            x_coodinate_course=-150+between_sections+course_count*150
            label_id=label+str(course_count)
            print(f"tasks count: {len(tasks)}")
            course_count+=1
            course_task_count=0
            for task in tasks:
                
                course_task_count+=1
                y_coodinate = 260 + course_task_count*80
                
                print(f"Task: {task}")
             
                add_task_to_xml(task.id, task.content, x_coodinate_course,y_coodinate,xml_file_path, colors[course_count-1], "0", "12", priority_colors[task.priority-1],5)
            task_count+=1
        
            add_task_to_xml(label_id, label, x_coodinate_course, 250 ,xml_file_path, colors[course_count-1], "1","14")
        between_sections+=50
        add_task_to_xml(section_id, str(section_name), x_coodinate_section, "120" ,xml_file_path, colors1[course_count-1], "1","14" )
    # for task in sorted_tasks:
    #     print(task)
    #     
    #     print(f"Taso 1: {task.section_id}")
    #     #print(f"Taso 2: {task.labels[0]}")
    #     print(f"Taso 3: {task.content}")
    
    #print(tasks[1].due.date)

if __name__ == "__main__":
    main()