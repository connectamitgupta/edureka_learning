'''Create a script called location that return the location parameters of any location you
want'''

import geocoder
g = geocoder.ip('me')
print(g.latlng)