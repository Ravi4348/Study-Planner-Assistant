from flask import Flask, render_template, request, redirect, url_for, session
from rag_engine import RAGEngine

app = Flask(__name__)
app.secret_key = "supersecretkey"   # Required for sessions

rag = RAGEngine()

# ---------------- LOGIN PAGE ---------------- #

USERNAME = "admin"
PASSWORD = "12345678"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


# ---------------- HOME PAGE (PROTECTED) ---------------- #

@app.route("/", methods=["GET", "POST"])
def index():
    # Protect route
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if request.method == "POST":
        date = request.form["date"]
        hours = request.form["hours"]
        subject = request.form["subject"]

        plan = rag.generate_plan(date, hours, subject)
        return render_template("plan.html", plan=plan)

    return render_template("index.html")


# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
