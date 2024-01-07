import xml.etree.ElementTree as ET
tree = ET.parse('./todoist_api/todoist_api_app/chart_copy.drawio')
root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)

# for country in root[0][0][0].findall('mxCell'):
#     print(country)

diagram = root.find(".//diagram/mxGraphModel/root")




   
# task_cell = diagram.findall("mxCell")

for neighbor in diagram.iter('mxGeometry'):
    print(neighbor.attrib)

# for cell in task_cell:
#     mxGraphModel = ET.SubElement(cell, "")
#     print(mxGraphModel)
    # geo=cell.find("mxGeometry")
    # print(geo.attrib)
# xmlRoot = tree.getroot()
# child = ET.Element("mxCell")
# diagram.append(child)
# task_cell.set("id", f"id34234")
# task_cell.set("value", "task.content")
# task_cell.set("style", "rounded=1;")  # Simplified style for demonstration
# task_geometry = ET.SubElement(task_cell, "mxGeometry")
# task_geometry.set("width", "120")
# task_geometry.set("height", "60")
# task_geometry.set("as", "geometry")


#tree.write('./todoist_api/todoist_api_app/chart_copy.drawio')

# root1 = ET.Element("mxfile")
# diagram = ET.SubElement(root1, "diagram")
# mxGraphModel = ET.SubElement(diagram, "mxGraphModel")
# root_element = ET.SubElement(mxGraphModel, "root")

print(diagram.tag)