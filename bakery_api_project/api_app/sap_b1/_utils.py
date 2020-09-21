import datetime
from flask.json import JSONEncoder
from decimal import Decimal

class fakefloat(float):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return str(self._value)
        
class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            # Subclass float with custom repr?
            return fakefloat(o)
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        raise TypeError(repr(o) + " is not JSON serializable")

def data_rows(rows):
    headers = ['SeriesName', 'DocNum', 'DocDate', 'DocDueDate', 'CardCode', 'CardName', 'Comments', 'U_Approved', 'U_Remarks', 'DocEntry']
    row_dict = {}
    for row in rows:
        docnum = row['DocNum']
        if docnum not in row_dict:
            row_dict[docnum] = {}
            row_dict[docnum]['Details'] = []
        # else:
        details = {}
        for key, val in row.items():
            if key not in row_dict[docnum] and key in headers:
                row_dict[docnum][key] = val
            elif key not in headers:
                details[key] = val
        row_dict[docnum]['Details'].append(details)
        
    return row_dict

