from flask import Flask, request, render_template, g, url_for, jsonify, flash
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
auth = ()


@app.route("/", methods=["GET"])
def index():
    context = {"key1": "value1"}

    return render_template(
        'index.html',
        context=context
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        debug=True, 
        port=5580
    )
