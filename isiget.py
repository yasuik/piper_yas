import requests
import json
import redis

r = redis.Redis(host='redis url', port='redis port', password='redis password')

# Isilon OneFS URL Set
isi = "https://192.168.1.111:8080"
uri = "/platform/3/cluster/nodes/1/status"
url = isi + uri

response = requests.get(url, auth=('root', 'a'), verify=False)

# Isilon OneFS API Get Status
obj = json.loads(response.content)
print "OneFS version: ", obj['nodes'][0]['release']
r.set("OneFS version", obj['nodes'][0]['release'])

print "Uptime: ", int(obj['nodes'][0]['uptime'])/60/60
r.set("Uptime", int(obj['nodes'][0]['uptime'])/60/60)

print "Capacity: ", obj['nodes'][0]['capacity'][0]['bytes']/1024/1024
r.set("Capacity", int(obj['nodes'][0]['capacity'][0]['bytes'])/1024/1024)
