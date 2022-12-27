import xml.etree.ElementTree as ET
import csv
tree = ET.parse(r"d:\My project\BlogApp\BlogApp\fedility_service\sample.xml")
print("----------------------------")
root = tree.getroot()
print("...................",root)
 
Resident_data = open(r'd:\My project\BlogApp\BlogApp\fedility_service\output.csv', 'w')
 
csvwriter = csv.writer(Resident_data)
resident_head = []
count = 0
for member in root.find('ReportData'):
    print(member)
    csvwriter.writerow([member.text, "empty"])
   
Resident_data.close()



