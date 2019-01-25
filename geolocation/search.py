import geocoder

ip = "[IP]"
g = geocoder.ip(ip)
print(g.json)
