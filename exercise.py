import requests

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
owr = ottawa_wards_response.json()

#Exercise 1
owr.keys()

objects = owr['objects']
objects.__class__

for ward in objects:
    print(ward['name'])

#Exercise 2
elections = requests.get('https://represent.opennorth.ca/elections/')
r = elections.json()

r.keys()

objects = r['objects']
objects.__class__
for e in objects:
    print(e['name'])
