import datetime
from flask import Blueprint, json, jsonify, request
from decimal import Decimal
from api_app import auth, create_app, db, cache
from ._utils import data_rows, CustomJSONEncoder
from .raw_query import it_query

class fakefloat(float):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return str(self._value)

def defaultencode(o):
    if isinstance(o, Decimal):
        # Subclass float with custom repr?
        return fakefloat(o)
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    raise TypeError(repr(o) + " is not JSON serializable")

sap_b1 = Blueprint('sap_b1', __name__)

@sap_b1.route('/api/get_it', methods=['GET'])
@cache.cached(timeout=5)
def get_it():
    # get the parameter and assign to variables
    docnum = request.args.get('docnum')
    fromwhse = request.args.get('fromwhse')

    # execute query
    raw_query =  db.get_engine(bind='pos').execute(it_query(docnum, fromwhse))
    
    # convert the result to dictionary and pass to data
    data = data_rows(raw_query)
    
    data_json = json.loads(json.dumps(data, default=defaultencode))
    response = jsonify(data_json)
    return response

# @sap_b1.route('/api/get_po', methods=['GET'])
# def get_po():

