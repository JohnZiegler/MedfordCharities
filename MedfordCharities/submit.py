from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import json
import requests
import gbmodel

class Submit(MethodView):
    def get(self):
        return render_template('submit.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to list when completed, to ensure information was added correctly.
        """
        formatted_address = request.form['address'].replace(" ","+")
        
        request_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + formatted_address + '&key=AIzaSyDrkycdV52v6SdQJ7RwN85QwzP5cNk3oF8'
        headers = {'Accept': 'application/json'}
        location_json_data = requests.get(request_url, headers=headers)
        location_json = json.loads(location_json_data.content)
        
        model = gbmodel.get_model()
        model.insert(request.form['name'],
                     request.form['description'],
                     request.form['address'],
                     request.form['typeOfCharity'],
                     request.form['phone'],
                     request.form['hours'],
                     request.form['reviews'],
                     location_json["results"][0]["geometry"]["location"]["lat"],
                     location_json["results"][0]["geometry"]["location"]["lng"])
        return redirect(url_for('list'))
