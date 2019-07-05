from flask import Flask, request, render_template, g, url_for, jsonify, flash, redirect
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta

app = Flask(__name__)
auth = ("admin", "admin")

@app.route("/", methods=["GET"])
def homepage():
    """ redirect to index """
    return redirect(url_for("index"))


@app.route("/index", methods=["GET"])
def index():
    """ Index page """
    path = request.path
    context = {"path": path}

    return render_template(
        'index.html',
        context=context
    )


@app.route("/flask", methods=["GET"])
def flask_apis():
    """ List of Flask RESTful APIs """

    apilist = ["Geolocate by IP Address", "Geolocate by Lat/Long", "Phone Number Location", "Street Address Validation", 
               "Email Address Deliverablity", "IP Address to Consumer Profile"]

    return render_template(
        "flask.html",
        context=apilist,
        today=get_date()
    )


@app.route("/sqlalchemy", methods=["GET"])
def alchemy():
    """ SQL Alchemy in Containers """
    context = {"key1": "value1"}
    
    return render_template(
        "flask.html",
        context=context,
        today=get_date()
    )

@app.route("/kubes", methods=["GET"])
def kubes():
    """ Kubernetes Orchestration """

    context = {"key1": "value1"}

    return render_template(
        "flask.html",
        context=context,
        today=get_date()
    )

@app.route("/okd", methods=["GET"])
def okd():
    """ OpenShift Container Platform"""

    context = {"key1": "value1"}

    return render_template(
        "flask.html",
        context=context,
        today=get_date()
    )


@app.route("/ipaddress/<string:ipaddr>", methods=["GET"])
def geolocate(ipaddr):
    """
    Geolocate an IP Address
    """
    
    url = "https://ipapi.co/" + str(ipaddr) + "/json/"
    method = "GET"
    hdr = {"content-type": "application/json", "user-agent": "SimplePythonFoo()"}

    try:
        r = requests.request(method, url, headers=hdr)

        if r.status_code != 200:
            flash("The API call returned HTTP Status Code: {}".format(str(r.status_code)))
            return redirect(url_for("index"))

        resp = r.json()

        return render_template(
            "geolocate.html",
            context=resp
        )

    except requests.HTTPError as http_err:
        flash("Geolocate API returned HTTP error: {}".format(str(http_err)))
        return redirect(url_for("index"))


@app.route("/login", methods=["GET"])
def login():
    """ Login the user """
    return render_template(
        "login.html",
        today=get_date()
    )

@app.route("/logout", methods=["GET"])
def logout():
    """
    Log out the user
    """
    pass


def convert_datetime_object(o):
    if isinstance(o, datetime):
        return o.__str__()


def get_date():
    # set the current date time for each page
    today = datetime.now().strftime('%c')
    return '{}'.format(today)


def compare_(a, b):
    return a == b


'''
******************************
******** Error Pages *********
******************************
'''


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(err):
    return render_template('500.html'), 500


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        debug=True, 
        port=5880
    )
