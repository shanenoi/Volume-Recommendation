from datas import control
from flask import Flask, request
from re import sub

import os
import time

app = Flask(__name__)
PWD = sub("([^/\.]+\.[^/\.]+)", "", os.path.realpath(__file__))


@app.route("/create/<id>")
def create(id):
    if control.check_id(id):
        return "0"
    else:
        control.DATA[id] = [[],[],0,0]
        control.Data().save()
        return "1"


@app.route("/check/<id>")
def check(id):
    if control.check_id(id):
        return "1"
    return "0"


@app.route("/upload/<id>", methods=['POST'])  # args: file, array
def upload(id):
    if request.method == "POST":
        fi = request.files['file']
        fi.save(PWD + "../datas/" + fi.filename)

        ary = eval('[' + request.form['array'] + ']')
        print(ary, PWD)

        ctr = control.Controller()
        ctr.key = id
        ctr.insert_new_data(
            control.pretreatment(
                PWD + "../datas/" + fi.filename,
                ary
            )
        )

        return "1"
    else:
        return "0"


@app.route("/recommendation/<id>")
def recommendation(id):
    if control.check_id(id):
        ctr = control.Controller()
        ctr.key = id
        vl = ctr.get_value()

        return ','.join(v1)

    else:

        return "0"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
