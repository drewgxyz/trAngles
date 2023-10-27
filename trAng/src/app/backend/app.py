from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api/data')
def get_data():
    data = {
        'title': 'trAng',
        'message': 'Testing Angular and Python with AWS Comprehend + cgpt'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()