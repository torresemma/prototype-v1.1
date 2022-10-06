from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('registry.html')

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run(host='0.0.0.0',port=4449)


