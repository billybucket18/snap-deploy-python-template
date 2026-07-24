from flask import Flask

requests = '0'
app = Flask(__name__)

@app.route('/')
def hello_world():
    requests = str(int(requests) + 1)
    return 'Hello from the example server! Request number: ' + requests

if __name__ == '__main__':
    app.run()
