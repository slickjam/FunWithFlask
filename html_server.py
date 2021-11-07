from flask import Flask, render_template

from activity import Activity

app = Flask(__name__)
activities = ["Chess", "Terraforming Mars", "Deep Rock Galactic"]

new_activities = [
        Activity("Wheel Of Fortune", "11/15 - 10:00 am", "Room C", "Pat"),
        Activity("Price is Right", "11/17 - 11:00 am", "Room P", "Bob"),
        Activity("Press Your Luck", "11/19 - 8:00 pm", "Room L", "Mrs. Banks")
    ]

@app.route("/")
def index():
    return render_template("index.html", activities=activities)

# setting the host to 0.0.0.0 makes it available to all machines on the network
app.run(host="0.0.0.0", port=5000, debug=True)