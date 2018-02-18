
import requests
import json

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']


print(j)

a = Patient('123444444','Dan', 'siddiqui','dob','sex','32323232','45mann','helth')
print(a.get_lastName)
