import csv
with open('departments.csv', newline='') as csvfile: 
   data=csv.DictReader(csvfile)
   print("Id  department name")
   print("...............")
   for col in data:
    print(col['department_id'], col['department_name'])
