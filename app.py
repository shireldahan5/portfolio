# app.py, Shirel Dahan portfolio
#
# Content that repeats (projects, links) lives here as plain Python data,
# and the templates decide how it looks.

import os

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


EMAIL = "shirel.dahan@mail.mcgill.ca"

LINKS = {
    "github": "https://github.com/shireldahan5",
    "linkedin": "https://linkedin.com/in/shireldahan",
}

# Selected work shown on the home page. Each project with a "slug"
# also has its own case study page at /work/<slug>.
PROJECTS = [
    {
        "slug": "swim",
        "title": "Swim with Shirel",
        "year": "2026",
        "summary": (
            "A booking site for the private swim lessons I have taught since 2020. "
            "Parents see open times, request a lesson in five short steps, "
            "and I confirm by email."
        ),
        "role": "Design and development",
        "stack": "Next.js, React, TypeScript, Tailwind CSS, SQLite",
        "live": "https://swim-with-shirel-production.up.railway.app/",
        "code": "https://github.com/shireldahan5/swim-with-shirel",
        "image": "img/work/swim-desktop.jpg",
        "image_alt": (
            "Swim with Shirel home page: a large navy serif headline reading "
            "'swim. with Shirel.' next to a photo of pool water."
        ),
    },
]


# Shared values available in every template
@app.context_processor
def site_globals():
    return {"email": EMAIL, "links": LINKS}


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS)


@app.route("/work/swim")
def work_swim():
    project = next(p for p in PROJECTS if p["slug"] == "swim")
    return render_template("work_swim.html", project=project)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Old pages from the previous version of the site. Redirect instead of
# 404ing in case someone saved or shared one of these links.
@app.route("/projects")
def old_projects():
    return redirect(url_for("index", _anchor="work"), code=301)


@app.route("/experience")
@app.route("/skills")
def old_about_pages():
    return redirect(url_for("about"), code=301)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # Local development only. Railway runs the app with gunicorn instead.
    app.run(debug=True, port=int(os.environ.get("PORT", 5050)))
