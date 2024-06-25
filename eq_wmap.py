from pathlib import Path
import json

import plotly.express as px

# Read data as string and convert to a python object.
path = Path('eq_data/eq_data_1_day_m1.json')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examin all earthquake in the dataset
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

print(mags[:12]) 
print(lons[:5]) 
print(lats[:5]) 

title = 'Global Earthquake'
fig = px.scatter_geo(lat=lats, lon=lons, title=title, 
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
