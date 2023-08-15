"""
A flask app for the listing of Medford Charities and Non-Profit Organizations
"""
import flask
from flask.views import MethodView
from index import Index
from submit import Submit
from list import List

app = flask.Flask(__name__)# our Flask app
# Adding url for our main page index site
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])
# Adding url for the submission page to add a charity
app.add_url_rule('/submit/',
                 view_func=Submit.as_view('submit'),
                 methods=['GET', 'POST'])
# Adding url for the listings page of currently added charities
app.add_url_rule('/list/',
                 view_func=List.as_view('list'),
                 methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
