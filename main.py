from flask import Flask, jsonify
from OpenSSL import SSL
app = Flask (__name__)

@app.route('/')
def main():
    return 'Hello World'

@app.route('/api/data', methods=['GET'])
def get_data():
    # Example data
    data = {
        "message": "This is a test to get data from flask",
    }
    return jsonify(data)


if __name__ == '__main__':
    context = ('/Users/nicholas/flask_csr.csr', '/Users/nicholas/flask.key')
    app.run(debug=True)