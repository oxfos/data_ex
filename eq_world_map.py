import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) # data converted into dictionary.

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquackes.
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquackes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquackes.html')