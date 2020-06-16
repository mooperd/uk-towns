import csv
from flask import Flask, jsonify

app = Flask(__name__)

def import_data(file_name):
    return_list = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                return_list.append(row)
    return return_list
    
@app.route('/')
def root_data():
    data = import_data('uk-towns-sample.csv')
    return jsonify(data)

@app.route('/type/<search_term>')
def by_county(search_term):
    data = import_data('uk-towns-sample.csv')
    return_list = []
    for row in data:
        if row["type"] == search_term:
            return_list.append(row)
    return jsonify(return_list)

if __name__ == '__main__':
    app.run(debug=True)




