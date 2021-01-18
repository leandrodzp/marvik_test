from utils import formated_date

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/date', methods=['POST'])
def date():
    date = formated_date(verbose())
    return jsonify(date)

# In case verbose param is missing simplified date is returned
def verbose():
    if 'verbose' in request.json:
        return request.json['verbose'] == True
    else:
        return False
    