"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student-search")
def get_student_form():
	"""Show form for searching for a student"""

	return render_template("student_search.html")

@app.route("/student-add", methods = ['GET', 'POST'])
def student_add():
	"""Show form for entering student info"""

# @app.route("/student-add", methods = ['POST'])
# def student_add_post():
# 	"""Add student info to hackbright database from student input form"""
	if request.method == 'POST':

		first_name = request.form['first_name']
		last_name = request.form['last_name']
		github = request.form['github']

		hackbright.make_new_student(first_name, last_name, github)

		return redirect("/student-add-success")
	else:
		return render_template("student_add_form.html")

@app.route("/student-add-success")
def student_add_success():
	"""Show successful student add"""

	return render_template("student_add_success.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
    						first=first,
    						last=last,
    						github=github)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
