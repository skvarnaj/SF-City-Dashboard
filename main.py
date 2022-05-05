from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', title = 'home')

@app.route("/dashboard")
def dashboard():
   return render_template('dashboard.html', title = 'SF Community Dashboard')

@app.route("/graphic")
def graphic():
    return render_template('graphic.html', title = 'Dark Side of SF Housing')

@app.route("/add")
def add():
    return render_template('add.html', title = 'What I would change and add')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


