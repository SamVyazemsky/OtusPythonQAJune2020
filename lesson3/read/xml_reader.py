from lxml import etree

import dicttoxml
import xmltodict
import xml.etree.ElementTree as ET

# tree = ET.parse('../data/data.xml')
# root = tree.getroot()
# #
# for child in root:
#     print(child.tag, child.attrib)
#     for _child in child:
#         print(_child.tag, _child.text)

# -------------------------
# with open('../data/data.xml', 'r') as file:
#     f = file.read()
#     new_dct = xmltodict.parse(f"""{f}""", )
#     print(dict(new_dct))

# -------------------------
# dct_ = {'test1': 123, 'test2': 345, 'test3': {'test1': 124, 'test4': 100500}}
# new = dicttoxml.dicttoxml(dct_)
# print(new)

# -------------------------
root_el = etree.Element('root')
r = etree.SubElement(root_el, 'root2')
# r.text = 'test12345'
etree.SubElement(r, 'child')
print(etree.tostring(root_el))
