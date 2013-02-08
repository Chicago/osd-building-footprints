# TITLE: Importing GeoJSON Example in Python
# AUTHOR: Tom Schenk Jr., City of Chicago
# CREATED: 2013-01-23
# UPDATED: 2013-02-03
# NOTES: Quick example to import GeoJSON data in Python.
# MODULES: json

import json
building_json = open('PATH/TO/FILE/data/Transportation.json', 'r')
building_footprints = json.load(json_data)
json_data.close()