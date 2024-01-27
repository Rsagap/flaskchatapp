from flask import Flask, render_template, redirect, request, session
# The Session instance is not used for direct access, you should always use flask.session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def index():
	#check if logged in yes->rooms.html
	#else ->index.html
	if not session.get("name"):
		return render_template("index.html")
	return render_template('rooms.html')


@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session["name"] = request.form.get("username")
		return redirect("/")
	return render_template("login.html")


@app.route("/join", methods=["POST", "GET"])
def join():
	if not session.get("name"):
		return render_template("index.html")
	return render_template('join-room.html')


@app.route("/create", methods=["POST", "GET"])
def create():
	if not session.get("name"):
		return render_template("index.html")
	return render_template('create-room.html')

@app.route("/chatroom", methods=["POST", "GET"])
def chatroom():
	if not session.get("name"):
		return render_template("index.html")
	return render_template('chat-room.html')



@app.route("/logout")
def logout():
	session["name"] = None
	return redirect("/")


if __name__ == "__main__":
	app.run(debug=True)
