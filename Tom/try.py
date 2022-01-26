# JSON file
f = open ('gamesTom.json', "r")
 
# Reading from file
data = json.loads(f.read())
 
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
 
# Closing file
f.close()