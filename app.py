# app.py, Shirel Dahan portfolio
#
# Content that repeats (projects, experience, awards, links) lives here
# as plain Python data, and the templates decide how it looks.

import os

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


EMAIL = "shirel.dahan@mail.mcgill.ca"
PHONE = "(438) 827-8376"

LINKS = {
    "github": "https://github.com/shireldahan5",
    "linkedin": "https://linkedin.com/in/shireldahan",
}

# Selected work shown on the home page. A project with a "slug" also
# has its own case study page at /work/<slug>.
PROJECTS = [
    {
        "slug": "swim",
        "number": "01",
        "title": "Swim with Shirel",
        "kind": "Swim lesson booking app",
        "date": "April 2026",
        "summary": (
            "A full-stack reservation platform for my swim lessons. Parents can book "
            "single, multi-session or recurring weekly lessons for several children "
            "in one booking, and every request goes through an admin approval step."
        ),
        "role": "Design, development and deployment",
        "stack": "Next.js, React, TypeScript, Tailwind CSS, SQLite, Railway",
        "live": "https://swim-with-shirel-production.up.railway.app/",
        "code": "https://github.com/shireldahan5/swim-with-shirel",
        "image": "img/work/swim-desktop.jpg",
        "image_mobile": "img/work/swim-mobile.jpg",
        "image_alt": (
            "Swim with Shirel home page: a large navy serif headline reading "
            "'swim. with Shirel.' next to a photo of pool water."
        ),
    },
    {
        "slug": None,
        "number": "02",
        "title": "POP",
        "kind": "AI patient care-plan platform",
        "date": "January 2026 – now",
        "summary": (
            "A web app from a two-person startup that uses AI to turn patients’ "
            "medical instructions into personalized care plans. I’m planning the "
            "architecture for a new chronic-conditions feature, which extends the app "
            "from post-surgical recovery to long-term condition support."
        ),
        "role": "Contributor",
        "stack": "Next.js, React, TypeScript, Supabase, Claude API",
        "live": "https://www.pophealth.ai/",
        "live_label": "pophealth.ai",
    },
]

EXPERIENCE = [
    {
        "role": "Study Hall Supervisor",
        "org": "JASS Tutors, Montreal",
        "dates": "2026 – now",
        "note": (
            "Manage a weekly after-school study hall for elementary students, "
            "overseeing homework help and tutors."
        ),
    },
    {
        "role": "Water Safety Instructor & Pool Lifeguard",
        "org": "Côte Saint-Luc Aquatic and Community Centre",
        "dates": "2022 – 2024",
        "note": (
            "Taught swimming and water safety to children and adults of all skill "
            "levels. Supervised swimmers and responded calmly to emergencies, "
            "following safety protocols."
        ),
    },
]

LEADERSHIP = [
    {
        "role": "Vice President of Social Media",
        "org": "Google Developer Groups McGill",
        "dates": "2026 – now",
        "note": (
            "Lead social media strategy and content promoting technical workshops, "
            "networking events and career opportunities to McGill students."
        ),
    },
    {
        "role": "President",
        "org": "Save A Child’s Heart McGill",
        "dates": "2025 – now",
        "note": "Direct an executive team to launch fundraising and awareness campaigns.",
    },
    {
        "role": "Volunteer First Responder",
        "org": "Magen David Adom, Israel",
        "dates": "Summer 2024",
        "note": "Assisted in emergency medical response, gaining teamwork and crisis management experience.",
    },
    {
        "role": "Volunteer",
        "org": "Chabad Care",
        "dates": "2023 – now",
        "note": "Support hospital staff and patients through fundraising and community initiatives.",
    },
]

AWARDS = [
    {
        "title": "Gilsig Family Scholarship for Studies in McGill Engineering",
        "from": "Jewish Community Foundation of Montreal, $3,500",
        "dates": "2025, 2026",
    },
]

SKILLS = [
    ("Programming", "Java, Python, C, HTML and CSS, Bash, VHDL"),
    ("Frameworks", "React, Next.js, Tailwind CSS, Flask, JUnit"),
    ("Tools", "Git and GitHub, Linux and Unix, SQLite, Railway, VS Code, IntelliJ, PyCharm, ModelSim"),
    ("AI-assisted", "Claude Code"),
    ("Spoken", "English (native), French (fluent), Hebrew (basic)"),
]

COURSES = [
    "Algorithms & Data Structures",
    "Software Systems (C, Unix, Bash)",
    "Fundamentals of Software Development (Java, OOP)",
    "Model-Based Programming",
    "Design Principles & Methods",
    "Digital Logic",
    "Discrete Structures",
]


# Shared values available in every template
@app.context_processor
def site_globals():
    return {"email": EMAIL, "phone": PHONE, "links": LINKS}


@app.route("/")
def index():
    # The home page shows the current roles as a short index
    now = [EXPERIENCE[0], LEADERSHIP[0], LEADERSHIP[1]]
    return render_template("index.html", projects=PROJECTS, now=now)


@app.route("/work/swim")
def work_swim():
    project = next(p for p in PROJECTS if p["slug"] == "swim")
    return render_template("work_swim.html", project=project)


# About is written, not listed. The CV-style details live on /experience.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/experience")
def experience():
    return render_template(
        "experience.html",
        experience=EXPERIENCE,
        leadership=LEADERSHIP,
        awards=AWARDS,
        skills=SKILLS,
        courses=COURSES,
    )


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Old pages from the first version of the site. Redirect instead of
# 404ing in case someone saved or shared one of these links.
@app.route("/projects")
def old_projects():
    return redirect(url_for("index", _anchor="work"), code=301)


@app.route("/skills")
def old_skills():
    return redirect(url_for("experience"), code=301)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # Local development only. Railway runs the app with gunicorn instead.
    app.run(debug=True, port=int(os.environ.get("PORT", 5050)))
