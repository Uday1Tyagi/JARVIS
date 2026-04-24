from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import hashlib
from flask import send_from_directory

app = Flask(__name__)
CORS(app)

USER_FILE = "users.json"


def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

@app.route("/")
def home():
    return send_from_directory(".", "home.html")

def save_users(data):
    with open(USER_FILE, "w") as f:
        json.dump(data, f, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# 🔥 REGISTER
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    email = data.get("email","").strip()
    password = data.get("password","").strip()
    name = data.get("name","").strip()
    dob = data.get("dob","").strip()

    users = load_users()

    if email in users:

        return jsonify({
            "status":"fail",
            "message":"User already exists"
        })


    users[email] = {

        "password": hash_password(password),

        "name": name,

        "dob": dob

    }


    save_users(users)


    return jsonify({
        "status":"success",
        "message":"Registered successfully"
    })

# 🔥 LOGIN
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email","").strip()
    password = data.get("password","").strip()

    users = load_users()

    if email in users:

        if users[email]["password"] == hash_password(password):

            return jsonify({

                "status":"success",

                "name": users[email]["name"],

                "dob": users[email]["dob"]

            })

    return jsonify({

        "status":"fail",

        "message":"Invalid credentials"

    })
from executor import execute
from command_engine import classify_command

@app.route("/process", methods=["POST"])
def process():

    data = request.get_json()

    query = data.get("query")

    email = data.get("email")

    users = load_users()

    name = users[email]["name"]


    intent = classify_command(query)

    response = execute(intent, query)


    return jsonify({

        "response": f" {response}"

    })

if __name__ == "__main__":
    app.run(debug=True)