import flask
from flask import jsonify
from reader import nfc_parse_items

app = flask.Flask(__name__)


@app.route('/api/items/<nfc_id>', methods=['GET'])
def get_items(nfc_id):
    try:
        items = nfc_parse_items(nfc_id)
        return jsonify(items)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
