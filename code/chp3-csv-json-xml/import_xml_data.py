from xml.etree import ElementTree as ET

tree = ET.parse('../../data/chp3/data-text.xml')
root = tree.getroot()
print (root)

data = root.find('Data')

all_data = []
#print list(root)
for observation in data:
    record = {}
    for item in observation:
        #print(item)
        #print(item.text)  打印Element节点的text属性
        #查看节点属性
        # print list(item)
       # print  (item.attrib)
       # lookup_key = item.attrib.keys()[0]
        lookup_key = list(item.attrib.keys())[0]

        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']

        record[rec_key] = rec_value
    all_data.append(record)

#print (all_data)
