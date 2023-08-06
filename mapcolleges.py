import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open('univ.json','r')

outfile = open('readable_university_data.json','w')

univ_data = json.load(infile)

school_names = []
school_addresses = []
longitude_list = []
latitude_list = []
male_enrollments = []
female_enrollments = []

# Loop through each university's data in the JSON array
for university in univ_data:
    # Extract the information for each university
    school_name = university.get("instnm")
    school_address = university.get("Institution's internet website address (HD2020)")
    longitude = university.get("Longitude location of institution (HD2020)")
    latitude = university.get("Latitude location of institution (HD2020)")
    male_enrollment = university.get("Graduation rate  men (DRVGR2020)")
    female_enrollment = university.get("Graduation rate  women (DRVGR2020)")

    # Append the extracted data to the corresponding lists
    school_names.append(school_name)
    school_addresses.append(school_address)
    longitude_list.append(longitude)
    latitude_list.append(latitude)
    male_enrollments.append(male_enrollment)
    female_enrollments.append(female_enrollment)

