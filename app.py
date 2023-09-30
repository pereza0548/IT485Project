from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    req = requests.get('API URL')
    data = json.loads(req.content)
    return render_template('index.html', data=data['fist tag of json file'])

if __name__ == '__main__':
    app.run(debug=True)

