from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return """<h1>Hello world!</h1><br>
                        <img src='static/mamamia.jpg'>"""


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=port)
    serve(app, host='0.0.0.0', port=5000)

