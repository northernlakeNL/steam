#!/usr/bin/env python3

# Import json module
import json

# Define json data
applicants ="""{
  "Scott C Aldridge": "Present",
  "Joe L Foss": "Present",
  "Clyde M Gold": "Present",
  "Monique C Doolittle": "Absent",
  "David M Volkert": "Present",
  "Israel M Oneal": "Present",
  "Elizabeth M Groff": "Absent"
}"""
# Initialize a counter
counter = 0
# load the json data
appList = json.loads(applicants)
# iterate json to find the list of absent applicant
for key in appList:
    if (appList[key] == 'Absent'):
  # Check the counter the print the message
        if (counter == 0):
            print("The following applicants are absent:")
    print(key)
    counter = counter + 1

# Print the message if no applicant is absent
if (counter == 0):
  print("All applicants are present")