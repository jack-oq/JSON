import json
import plotly

infile = open('schools.geojson','r')

outfile = open('readable_university_data.json','w')

univ_data = json.load(infile)

print(type(univ_data))

json.dump(univ_data, outfile, indent=4)

list_of_univs = univ_data['features']

print(len(list_of_univs))

enrollment, lons, lats = [],[],[]

for univ in list_of_univs:
    lon = univ['geometry']['coordinates'][0]
    lat = univ['geometry']['coordinates'][1]

    lons.append(lon)
    lats.append(lat)

print(lons[:5])
print(lats[:5])
