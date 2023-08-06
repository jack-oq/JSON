import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

univ_file = open('univ.json', 'r')
univ_data = json.load(univ_file)

schools_file = open('schools.geojson', 'r')
schools_data = json.load(schools_file)

school_names = []
longitude_list = []
latitude_list = []
total_enrollment_list = []
male_enrollments = []
female_enrollments = []

for university in univ_data:
    if university.get("NCAA", {}).get("NAIA conference number football (IC2020)") == 108:
        school_name = university.get("instnm")
        longitude = university.get("Longitude location of institution (HD2020)")
        latitude = university.get("Latitude location of institution (HD2020)")
        women_percentage = university.get("Percent of total enrollment that are women (DRVEF2020)")
        total_enrollment = university.get("Total  enrollment (DRVEF2020)")
        women_enrollment = int(total_enrollment * (women_percentage / 100))
        men_enrollment = total_enrollment - women_enrollment

        school_names.append(school_name)
        longitude_list.append(longitude)
        latitude_list.append(latitude)
        total_enrollment_list.append(total_enrollment)
        male_enrollments.append(men_enrollment)
        female_enrollments.append(women_enrollment)

school_addresses = []
for feature in schools_data["features"]:
    address = feature["properties"]["STREET"]
    school_addresses.append(address)

hover_text = []
for i in range(len(school_names)):
    name = school_names[i]
    address = school_addresses[i]
    total = total_enrollment_list[i]
    male = male_enrollments[i]
    female = female_enrollments[i]
    #<br> makes a new line like \n
    text = f"{name}<br>{address}<br>Total Enrollment: {total:,}<br>Male: {male:,}<br>Female: {female:,}"
    hover_text.append(text)

data = [
    {
        'type': 'scattergeo',
        'lon': longitude_list,
        'lat': latitude_list,
        'text': hover_text,
        'hoverinfo': 'text',
        'marker': {
            'size': [3 + .0002 * total_enrollment for total_enrollment in total_enrollment_list],
            'color': total_enrollment_list,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Enrollment'}
        }
    }
]

my_layout = Layout(title='Enrollment Information for Big 12 Universities')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='schools_data.html')
