from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class List(MethodView):

    def get(self):
        model = gbmodel.get_model()
        charities = [dict(name=row[0], description=row[1], address=row[2], typeOfCharity=row[3], phone=row[4], hours=row[5], reviews=row[6], latitude=row[7], longitude=row[8] ) for row in model.select()]
        return render_template('list.html',charities=charities)
