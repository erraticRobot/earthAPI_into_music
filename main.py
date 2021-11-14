import requests
import json
from datetime import datetime
import time
#  Unix epoch at 1 January 1970 00:00:00

# significant within hour
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson

# significant within the day
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson

# response = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson')
# response = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson')
response = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson')

# Dictionary keys for itm.properties
#dict_keys(['mag', 'place', 'time', 'updated', 'tz', 'url', 'detail', 'felt', 'cdi', 'mmi', 'alert', 'status', 'tsunami', 'sig', 'net', 'code', 'ids', 'sources', 'types', 'nst', 'dmin', 'rms', 'gap', 'magType', 'type', 'title'])

#
'''
What time keys contain. (NOTE: All times use ISO8601 Date/Time format. Unless a timezone is specified, UTC is assumed. )

1. endtime         present time        Limit to events on or before the specified end time.

2. start time      Now - 30 days       Limit to events on or after the specified start time. 

3. updated after   null                Limit to events updated after the specified time.
'''



print(response.status_code)
list = list(response.json()['features'])
list.reverse()

for l in list:
    # print(l['properties'].keys())
    magnitude = l['properties']['mag']
    curr_time = l['properties']['time']
    updated_time = l['properties']['updated']
    gap = l['properties']['gap']
    magnitude_type = l['properties']['magType']
    type1 = l['properties']['type']

    curr_time = time.gmtime(curr_time / 1000)
    updated_time = time.gmtime(updated_time / 100)

    print(f"magnitude: {magnitude}, time of uccurrence: {time.asctime(curr_time)}, updated_time: {time.asctime(updated_time)}, gap: {gap}, magnitude_type: {magnitude_type}, type: {type1}")

