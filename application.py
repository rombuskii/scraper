from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import scrape
import csv

application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'

@application.route("/", methods= ['GET'])
@cross_origin()
def origin():
    return render_template('form.html')

@application.route("/data", methods= ['POST'])
@cross_origin()
def data():
    item = request.form.get('item')
    scrape.getItems(item)
    with open('products.csv','r') as f:
        reader = csv.reader(f)
        return render_template("csv_table.html", csv=reader)


if(__name__ == "__main__"):
    from waitress import serve
    serve(application, host="0.0.0.0", port=5000)


