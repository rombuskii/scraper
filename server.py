from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import scrape
import csv

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods= ['GET'])
@cross_origin()
def origin():
    return render_template('form.html')

@app.route("/data", methods= ['POST'])
@cross_origin()
def data():
    item = request.form.get('item')
    scrape.getItems(item)
    with open('products.csv','r') as f:
        reader = csv.reader(f)
        return render_template("csv_table.html", csv=reader)


if(__name__ == "__main__"):
    app.run(debug=True)


