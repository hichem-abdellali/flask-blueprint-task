"""General page routes."""
from flask import current_app as app

from flask import Blueprint
from flask import request
from flask import render_template
import time

from ..forms import SearchForm

# Api map import
import json
import urllib
import requests

# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET", "POST"])
def http():
    form = SearchForm()

    # in case of initial load of the page with no request from the user yet
    if request.method == "POST" and form.validate():

        """prepare the link with necessary parameters to communicate
        with the yandex geoencoder and request the localisation coordinates
        longitude and latitude"""
        base_url = "https://geocode-maps.yandex.ru/1.x/?"
        parameters = {"geocode": request.form['address_form'],
                      "format": "json",
                      "lang": "en_US",
                      "apikey": app.config["AUTH_KEY"]}

        # handle any error during the process of the data
        try:

            r = requests.get(f"{base_url}{urllib.parse.urlencode(parameters)}")
            data = json.loads(r.content)
            position = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()

        # if any error ask the user to check his inout data
        except IndexError:
            return render_template(
                "index_map.jinja2",
                form=form,
                error_msg='please check your input',
                title="Distance from the MKAD to a specified address",
                subtitle="Type your address here",
            )

        # in case of successful response return the position to the view
        return render_template(
            "index_map.jinja2",
            form=form,
            geo_pose=position,
            address=request.form['address_form'],
            title="Distance from the MKAD to a specified address",
            subtitle="Type your address here",
        )
    else:
        return render_template(
            "index_map.jinja2",
            form=form,
            title="Distance from the MKAD to a specified address",
            subtitle="Type your address here",
        )


# rout for writing data into the log file
@home_bp.route("/write_log", methods=["POST"])
def write_log():
    data = request.get_json()

    # check if the data is complete
    if 'address' in data:

        # open the log file in append mode and write the time, input and result
        fo = open("data.log", "a")
        file_buffer = time.strftime('%A %B, %d %Y %H:%M:%S') + '; request: ' + data['address'] + ', Results: ' + str(
            data['distance']) + 'Km' + '\n'
        fo.writelines(file_buffer)
        fo.close()

        # return that the writing request was successful
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    else:
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}

