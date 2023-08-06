import json

infile = open('schools.geojson','r')

outfile = open('readable_university_data.json','w')

univ_data = json.load(infile)

print(type(univ_data))

json.dump(univ_data, outfile, indent=4)


