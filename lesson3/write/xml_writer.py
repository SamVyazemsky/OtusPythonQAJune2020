import xml.etree.ElementTree as ET

data = ET.Element('data')
items = ET.SubElement(data, 'root1')
item1 = ET.SubElement(items, 'root2')
item2 = ET.SubElement(items, 'root3')
item1.set('name', 'attr1')
item2.set('name', 'attr2')
item1.text = 'test1'
item2.text = 'test2'

# create a new XML file with the results
mydata = ET.tostring(data)
print(mydata)

# myfile = open("items2.xml", "w")
# myfile.write()
with open("items2.xml", "w") as file:
    file.write(mydata)
