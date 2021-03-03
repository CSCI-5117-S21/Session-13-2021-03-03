from flask import *
import db;

app = Flask(__name__)

@app.before_first_request
def initialize():
    db.setup()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hobby", methods=['POST'])
def new_hobby():
    name = request.form.get("name", "noname")
    desc = request.form.get("description", "no description")
    with db.get_db_cursor(True) as cur:
        cur.execute("INSERT INTO hobby (name, description) VALUES (%s, %s);", (name, desc))
    return "ok"


@app.route("/hobby", methods=['GET'])
def hobby_list():
    pass
