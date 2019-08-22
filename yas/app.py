#!/usr/bin/env python3
import os
import redis
import json
from flask import Flask, render_template, redirect, request, url_for, make_response, jsonify

if 'VCAP_SERVICES' in os.environ:
    VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
    CREDENTIALS = VCAP_SERVICES["rediscloud"][0]["credentials"]
    r = redis.Redis(host=CREDENTIALS["hostname"], port=CREDENTIALS["port"], password=CREDENTIALS["password"])
else:
    r = redis.Redis(host='127.0.0.1', port='6379')

app = Flask(__name__)

@app.route('/startapp')
def startapp():

    global r
    response = "<HTML><BODY>----------------------------------------------------<h1>Isilon SE Lab Manager</h1>"
    response += "----------------------------------------------------" + "<h2>Lab Environment</h2>"
    response += "<h3>Temperature : " + str(r.get('temp')) + " C" + "<br>Humidity    : " + str(r.get('humid')) + " %</h3>"
    response += "<h2>Isilon Cluster Status</h2>"
    response += "<h3>OneFS Version : " + str(r.get('OneFS version')) + "<br>Uptime : " + str(r.get('Uptime')) + " hours"
    response += "<br>Capacity : " + str(r.get('Capacity')) + " MBytes<br></h3></BODY>"

    return response

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', \
                port=int(os.getenv('PORT', '5000')), threaded=True)
