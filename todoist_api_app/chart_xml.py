import xml.etree.ElementTree as ET
from todoist_api_python.api import TodoistAPI
    #muuttujat
from muuttujat import *

api_key = TodoistAPI(TODOIST_API_KEY)

class Chart:
    def __init__(self, task_id:str, task_content:str, x_coodinate_course:int, y_coodinate:int, xml_file_path: str, fillcolor:str, fontstyle:int=0, fontsize:int=12, bordercolor: str="#000000", borderwidth:int=0, width:str="120", height:str="60"):
        self.task_id = task_id
        self.task_content = task_content
        self.x_coodinate_course = x_coodinate_course
        self.y_coodinate = y_coodinate
        self.xml_file_path = xml_file_path
        self.fillcolor = fillcolor
        self.fontstyle = fontstyle
        self.fontsize = fontsize
        self.bordercolor = bordercolor
        self.borderwidth = borderwidth
        self.width = width
        self.height = height

######################################################################################################## API related functions
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

######################################################################################################## XML related functions
def add_task_to_xml(item_object: Chart):
    """
    Adds a task to an XML file.

    Parameters:
     - item_object (Chart): An object containing the task details:
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
    tree = ET.parse(item_object.xml_file_path)
    root = tree.getroot()

    #Element where we will insert the new cell
    diagram = root.find(".//diagram/mxGraphModel/root")
    
    # mxCell element
    task_cell = ET.Element("mxCell")
    task_cell.set("id", item_object.task_id)
    task_cell.set("value", item_object.task_content)
    task_cell.set("style", f"whiteSpace=wrap;rounded=1;shadow=1;fillColor={item_object.fillcolor};strokeColor=none;fontColor=#FFFFFF;fontStyle={item_object.fontstyle};fontSize={item_object.fontsize};strokeWidth={item_object.borderwidth};strokeColor={item_object.bordercolor};")
    task_cell.set("parent", "1")
    task_cell.set("vertex", "1")

    # mxGeometry element
    geometry = ET.SubElement(task_cell, "mxGeometry")
    geometry.set("x", str(item_object.x_coodinate_course))
    geometry.set("y", str(item_object.y_coodinate))
    geometry.set("width", item_object.width)
    geometry.set("height", item_object.height)
    geometry.set("as", "geometry")

    # Append the new cell to the diagram
    diagram.append(task_cell)

    # Write back to the file
    tree.write(item_object.xml_file_path)


def main():

    ## Setting up variables
    xml_file_path = './todoist_api/todoist_api_app/chart_copy.drawio'
    section_count=0
    task_count=1
    subtask_count=1
    course_count=1
    between_sections=0
    colors=["#ED9B09","#326CAD","#0974ED","#987639","#3B536E"]
    colors1=["#F007DA","#55B031","#4AF008","#9B3891","#4A703B"]
    priority_colors=["#FFFFFF","#3cb371","#ffa500","#ff0000"]
    color_index=0

    ## Getting data from Todoist
    projects=get_all_projects(api_key)
    tasks=get_all_active_tasks(api_key)
    project_id = find_item_id(projects, "Inbox")
    sections=get_all_sections(api_key, project_id)
    
    ## Sorting tasks by due date
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
    
    #Processing each section, label and task. Adding them to the chart.
    for section_id, labels in tasks_by_section_and_label.items():
        print(f"Section ID: {section_id}")
        section_count+=1
        section_name = find_item_name(sections, section_id)
        x_coodinate_section=20+(course_count/2)*260
        
        for label, tasks in labels.items():
            
            print(f"Label: {label}")
            x_coodinate_course=-150+between_sections+course_count*250
            label_id=label+str(course_count)
            print(f"tasks count: {len(tasks)}")
            course_count+=1
            course_task_count=0
            color_index = (color_index + 1) % len(colors)
            

            for task in tasks:
                course_task_count+=1
                y_coodinate = 260 + course_task_count*100
                #Adding tasks and subtasks to the chart
                if task.parent_id == None:

                    #print(f"Task: {task}")
                    task_chart=Chart(
                        task_id=task.id,
                        task_content=task.content,
                        x_coodinate_course=x_coodinate_course,
                        y_coodinate=y_coodinate,
                        xml_file_path=xml_file_path,
                        fillcolor=colors[color_index],
                        fontstyle="0",
                        fontsize="12",
                        bordercolor=priority_colors[task.priority-1],
                        borderwidth="5",
                        width="120",
                        height="60"

                    )

                    add_task_to_xml(task_chart)
                else:
                    subtask_count+=1
                   
                    print(f"Subtask: {task}")
                    subtask_chart=Chart(
                        task_id=task.id,
                        task_content=task.content,
                        x_coodinate_course=x_coodinate_course+50,
                        y_coodinate=y_coodinate,
                        xml_file_path=xml_file_path,
                        fillcolor=colors[color_index],
                        fontstyle="0",
                        fontsize="12",
                        bordercolor=priority_colors[task.priority-1],
                        borderwidth="5",
                        width="120",
                        height="50"

                    )

                    add_task_to_xml(subtask_chart)
            task_count+=1
            course=Chart(
                task_id=label_id,
                task_content=label,
                x_coodinate_course=x_coodinate_course-10,
                y_coodinate=250,
                xml_file_path=xml_file_path,
                fillcolor=colors[color_index],
                fontstyle="1",
                fontsize="14",
                bordercolor="#000000",
                borderwidth="0",
                width="140",
                height="60"
            )
            add_task_to_xml(course)
        
        section=Chart(
            task_id=section_id,
            task_content=str(section_name),
            x_coodinate_course=x_coodinate_section+between_sections*1.5,
            y_coodinate=120,
            xml_file_path=xml_file_path,
            fillcolor=colors1[color_index],
            fontstyle="1",
            fontsize="14",
            bordercolor="#000000",
            borderwidth="0",
            width="160",
            height="60"
        )
        add_task_to_xml(section)
        between_sections+=150
    print(f"We are done. {section_count} sections and {task_count} tasks added to the chart.")

if __name__ == "__main__":
    main()