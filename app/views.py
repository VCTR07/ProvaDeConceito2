from flask import render_template, request, Flask

from app import app

import datetime

@app.route('/hora')
def horas():
    return str(datetime.datetime.now())

@app.route('/soma/<n1>/<n2>')
def my_form_post(n1,n2):
    

    return f"a soma dos dois numero deu {float(n1) + float(n2)}"
