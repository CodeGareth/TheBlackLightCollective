from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing():

    return render_template("home_page.html")

@app.route('/project_details')
def project_details():

    return render_template("project_details.html")
    
@app.route('/project')
def project():

    return render_template("project.html")


if __name__ == "__main__":
    app.run(debug = True)