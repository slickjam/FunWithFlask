from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask"

# add support for last name
@app.route("/<name>")
def hello(name):
    return f'Hello {name}'


# setting the host to 0.0.0.0 makes it available to all machines on the network
app.run(host="0.0.0.0", port=5000, debug=True)