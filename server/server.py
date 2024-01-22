import json
from flask import Flask, redirect  
from flask_cors import CORS
import requests
from dummy_data import dummy_data
import re
from datetime import datetime, timedelta

lastData = None
lastUpdate = datetime.min

app = Flask(__name__)     
CORS(app)



@app.route("/") 
def home():
    return redirect('api')

@app.route("/api")           
def api():       
    global lastUpdate, lastData
    if datetime.now() - lastUpdate < timedelta(minutes=5):
        print('use cache', datetime.now() - lastUpdate)
        return lastData

    req = requests.get('https://www.cwa.gov.tw/V8/C/W/Observe/MOD/24hr/A0C41.html')
    rawData = req.text
    # rawData = dummy_data

    # print(req.text)
    times = re.findall(r'<th scope="row" headers="time" class="is_show">([0-9][0-9]\/[0-9][0-9])<br class="visible-md"> ([0-9]+\:[0-9]+)<\/th>', rawData)
    temps = re.findall(r'<span class="tem-C is-active">([0-9]*[.][0-9])<\/span>', rawData)
    
    output = []
    for i in range(len(times)):
        output.append({
            "date": times[i][0],
            "time": times[i][1],
            "temp": float(temps[i])
        })

    lastData = output
    lastUpdate = datetime.now()

    return output # "<h1>hello world</h1>"   

app.run()