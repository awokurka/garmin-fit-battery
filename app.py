from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from fitparse import FitFile
import os
import subprocess
import json

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "temp/"
app.config["MAX_CONTENT_PATH"] = 5000000

@app.route('/')
def upload():
    return render_template('index.html')

@app.route('/display', methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)
        #file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        process = subprocess.run('fitdump ./temp/'+filename+' -n device_info -t json', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        output = process.stdout
        data = json.loads(output)
        content = {}
        for i in range(len(data)):
            index = (data[i]['data']['device_index'])
            version = (data[i]['data']['software_version'])
            manufacturer = (data[i]['data']['manufacturer'])
            serial = (data[i]['data']['serial_number'])
            battery_status = (data[i]['data']['battery_status'])
            battery_voltage = (data[i]['data']['battery_voltage'])
            timestamp = (data[i]['data']['timestamp'])
            content[i] = {
                "index": index,
                "version": version,
                "manufacturer": manufacturer,
                "serial": serial,
                "battery_status": battery_status,
                "battery_voltage": battery_voltage,
                "timestamp": timestamp
            }

        os.remove("./temp/"+filename)
        #print(content)
    return render_template('content.html', len = len(content), content=content) 


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    