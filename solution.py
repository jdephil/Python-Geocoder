import geocoder

destinations = [
'Space Needle',
'Crater Lake',
'Golden Gate Bridge',
'Yosemite National Park',
'Las Vegas, Nevada',
'Grand Canyon National Park',
'Aspen, Colorado',
'Mount Rushmore',
'Yellowstone National Park',
'Sandpoint, Idaho',
'Banff National Park',
'Capilano Suspension Bridge'
]



for point in destinations:
  coords = geocoder.arcgis(point)

  print(destinations[0] coords.latlng)