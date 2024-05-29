from flask import Flask, render_template, request, send_file
import random

app = Flask(__name__) # Create the server object variable
app.config['SECRET_KEY'] = str(random.randint(0,100000000))

@app.route("/")
def main_page():
    return send_file("main.html")

@app.route("/process", methods=['POST'])
def form_process():
    received = dict(request.values)
    text1 = received['text1'] # Dictionary key is the 'name' attribute in HTML
    # Do whatever processing you want with the data
    print("The user sent",text1)
    # Send a response
    return render_template("response.html", info=text1)

if __name__ == "__main__":
    # Start Flask webserver
    app.run(host="0.0.0.0", port=80, debug=True)