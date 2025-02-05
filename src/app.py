import flask
from flask import jsonify
from reader_nfc import nfc_parse_items
from google_sheet import save_data_to_spreadsheet

app = flask.Flask(__name__)


@app.route('/api/items/<nfc_id>', methods=['GET'])
def get_items(nfc_id):
    try:
        items = nfc_parse_items(nfc_id)
        return jsonify(items)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/items/<nfc_id>', methods=['POST'])
def nfc_data_to_spreadsheet(nfc_id):
    try:
        save_data_to_spreadsheet(nfc_id)
        return ("OK"), 204
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400  


if __name__ == '__main__':
    app.run(debug=True)
