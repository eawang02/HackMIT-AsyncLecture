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

    saveQuestion(output)
    return result

def refresh():
    question_file = open(r"questions.txt", "r")
    raw = question_file.readlines()
    questions = []

    for x in raw:
        questions.append(json.loads(x))    

    questions = sorted(questions, key=lambda i: i['time'])
    print(questions)

    return

def saveQuestion(q):
    question_file = open(r"questions.txt", "a+")
    question_dict = json.loads(q)

    question_file.write(json.dumps(question_dict) + "\n")

    question_file.close()
    return