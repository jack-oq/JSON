import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open('schools.geojson','r')

outfile = open('readable_university_data.json','w')

univ_data = json.load(infile)

print(type(univ_data))

json.dump(univ_data, outfile, indent=4)

list_of_univs = univ_data['features']

print(len(list_of_univs))

enrollment, lons, lats, hover_texts = [],[],[],[]

for univ in list_of_univs:
    #if univ['features']['properties'][]
    lon = univ['geometry']['coordinates'][0]
    lat = univ['geometry']['coordinates'][1]
    name = univ['properties']['NAME']

    lons.append(lon)
    lats.append(lat)
    hover_texts.append(name)

print(lons[:5])
print(lats[:5])

#data = [Scattergeo(lon=lons,lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{
        #size
        #color
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Enrollment'}
    }
}]

my_layout = Layout(title='Universites')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='schools_data.html')
