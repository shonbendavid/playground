# This is a sample Python script.
from flask import Flask
from flask import Flask
import os
import sys
from subprocess import Popen, PIPE, STDOUT
import json
import threading

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return Dict

outfile = open("test.json", "a", encoding="utf-8")



def is_json(myjson):
    try:
        data = json.loads(myjson)

        name = data["event_type"]
        if name in Dict:
            Dict[name] += 1
        else:
            Dict[name] = 1

        outfile.write(myjson)

    except ValueError as e:
        return False
    return True



if __name__ == '__main__':
    Dict = {}

    script_path = os.path.join("./", 'producer.py')
    p = Popen([sys.executable, '-u', script_path],
              stdout=PIPE, stderr=STDOUT, bufsize=1)
    threading.Thread(target=app.run, args=()).start()
    with p.stdout:
        for line in iter(p.stdout.readline, b''):

            threading.Thread(target=is_json, args=(line.decode('UTF-8'),)).start()

    p.wait()

