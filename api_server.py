from flask import Flask, request

app = Flask(__name__)

@app.route("/adduser", methods = ['GET', 'POST'])
def add_user():
    name = None
    if request.method == 'POST':
         name = request.args.get('name')
    
    if name != None:
        return f'Welcome {name}!'
    return 'Something went wrong, please try again or reach out to help for support.'

@app.route("/addsuperuser", methods = ['GET', 'POST'])
def add_super_user():
    name = None
    if request.method == 'POST':
        if request.headers.get('auth_code') == '8675309':
            name = request.args.get('name')
        else:
            return "Access Denied"
    
    if name != None:
        return f'Welcome Super User {name}!'
    return 'Something went wrong, please try again or reach out to help for support.'


# setting the host to 0.0.0.0 makes it available to all machines on the network
app.run(host="0.0.0.0", port=5000, debug=True)