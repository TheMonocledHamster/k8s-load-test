from crypt import methods
from  flask import Flask, Response, request, jsonify, redirect, session
from .load import load_cpu
from .errors import errors


app = Flask(__name__)
app.register_blueprint(errors)

@app.route("/load/cpu", methods=["GET"])
def cpu():
    load_cpu()
    return Response("Complete",status=200)

@app.route("/heartbeat", methods=["GET"])
def heartbeat():
    return Response("OK",status=200)

