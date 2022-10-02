from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    refresh()
    return render_template("index.html")

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    result = json.loads(output) #this converts the json output to a python dictionary
    print(result) # Printing the new dictionary
    print(type(result))#this shows the json converted as a python dictionary
    saveQuestion(result)

    return result

def refresh():
    # Open questions.txt and parse data
    # Create queue of questions to post on video
    # Send queue to JS frontend
    questions_File = open(r"questions.txt", "r")


    questions_File.close()
    return

def saveQuestion(q):
    questions_File = open(r"questions.txt", "a+")
    questions_File.write(q)

    questions_File.close()
    return