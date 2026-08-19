# ══════════════════════════════════════════════════════════════════
#  app.py, Shirel Dahan Portfolio
#  Built with Flask (Python web framework)
#
#  HOW THIS FILE WORKS:
#  Flask maps URL paths (like "/about") to Python functions.
#  Each function either passes data to an HTML template or
#  handles a form submission (like the contact form).
#  The templates live in the /templates/ folder.
# ══════════════════════════════════════════════════════════════════

import os
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask app.
# __name__ tells Flask where to look for templates and static files.
app = Flask(__name__)

# Secret key is required for Flask's "flash" message system (form feedback).
# os.environ.get() reads from environment variables, this is how you keep
# secrets out of your code. On Render, set SECRET_KEY in the dashboard.
# The second argument is the fallback used when running locally.
app.secret_key = os.environ.get("SECRET_KEY", "sd-portfolio-local-dev-only")


# ──────────────────────────────────────────────────────────────────
# ROUTES
# Each @app.route(...) decorator connects a URL to a function.
# ──────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Home page, hero section + intro highlights."""
    return render_template("index.html")


@app.route("/about")
def about():
    """About page, personal introduction and background."""
    return render_template("about.html")


@app.route("/experience")
def experience():
    """
    Experience page, work, education, volunteer, and awards.

    Instead of hard-coding data inside the HTML, we define it here as
    Python lists of dictionaries. Then we pass it to the template using
    render_template(). Inside the HTML, Jinja2 loops over these lists.

    This is a clean pattern: content lives in Python, layout lives in HTML.
    """

    # Each dict is one experience entry. To add a new one, just append.
    experiences = [
        {
            "category": "EDUCATION",
            "date": "2025 to 2029",
            "title": "B.Eng. Software Engineering (Co-op)",
            "organization": "McGill University",
            "location": "Montréal, QC",
            "description": (
                "Pursuing a co-operative degree in Software Engineering, building strong "
                "technical foundations across systems, algorithms, and engineering practice, "
                "with real-world industry placements woven throughout."
            ),
        },
        {
            "category": "ENGINEERING",
            "date": "2025 to Present",
            "title": "Member, Electrical Division",
            "organization": "McGill Formula Electric",
            "location": "Montréal, QC",
            "description": (
                "Collaborating with a multidisciplinary engineering team to design and "
                "optimize electric vehicle systems for competitive formula racing. Applying "
                "circuit analysis, digital logic, and systems thinking in a high-stakes, "
                "version-controlled environment."
            ),
        },
        {
            "category": "BUILDING",
            "date": "2025 to Present",
            "title": "AI-Assisted Engineering",
            "organization": "Self-Directed Exploration",
            "location": "Montréal, QC",
            "description": (
                "Actively building proficiency with Claude Code and Claude Cowork as core "
                "engineering tools. Using AI-assisted workflows to accelerate learning, write "
                "cleaner code, and tackle projects that would otherwise be out of reach for "
                "a first-year student. This portfolio is one example."
            ),
        },
        {
            "category": "BUILDING",
            "date": "2025 to Present",
            "title": "Web Development: HTML, CSS and Flask",
            "organization": "Self-Directed Projects",
            "location": "Montréal, QC",
            "description": (
                "Designing and building web projects from scratch using HTML, CSS, and Python/Flask. "
                "Focused on visual design systems, responsive layouts, and the craft of making "
                "things that feel as good as they function."
            ),
        },
        {
            "category": "OPEN SOURCE",
            "date": "2026 to Present",
            "title": "Contributor",
            "organization": "POP, Perioperative Care Plan",
            "location": "Remote",
            "description": (
                "Lightly contributing to POP, a multilingual patient-facing care-plan prototype for "
                "the perioperative journey. Patients upload hospital instructions as a PDF, photo, or "
                "audio recording, and POP turns that source material into a structured plan covering "
                "medications, restrictions, events, guidance, questions, education, and day-to-day "
                "follow-through. The interface currently supports English and Quebec French, with more "
                "languages planned."
            ),
        },
    ]

    awards = [
        {
            "title": "Gilsig Family Scholarship for Studies in McGill Engineering",
            "year": "2025",
            "description": "Merit-based scholarship awarded to exceptional incoming engineering students at McGill.",
        },
        {
            "title": "Health Science Honours List",
            "year": "2024",
            "description": "Recognized for academic excellence, the foundation of strong technical work.",
        },
        {
            "title": "Frank Cwilich Prize",
            "year": "2024",
            "description": "Awarded for outstanding academic achievement.",
        },
        {
            "title": "Director's Award",
            "year": "2024",
            "description": "Presented in recognition of exceptional performance and dedication.",
        },
    ]

    # Pass both lists to the template as named variables
    return render_template("experience.html", experiences=experiences, awards=awards)


@app.route("/skills")
def skills():
    """Skills page, technical abilities, tools, and certifications."""

    # Group skills by category, easy to edit and extend
    skill_groups = [
        {
            "category": "AI TOOLS",
            "index": "01",
            "skills": [
                "Claude Code", "Claude Cowork", "Anthropic API",
                "Prompt Engineering", "AI-Assisted Development", "Claude Projects",
            ],
        },
        {
            "category": "WEB & FRONTEND",
            "index": "02",
            "skills": [
                "HTML5", "CSS3", "Responsive Design",
                "CSS Custom Properties", "Flask (Python)", "Jinja2 Templates",
            ],
        },
        {
            "category": "PROGRAMMING",
            "index": "03",
            "skills": [
                "Python", "Java", "Bash / Terminal",
                "Probability & Statistics", "Discrete Mathematics", "Digital Logic",
            ],
        },
        {
            "category": "TOOLS & WORKFLOW",
            "index": "04",
            "skills": [
                "Git & GitHub", "VS Code", "PyCharm",
                "IntelliJ IDEA", "Debugging", "Technical Writing",
            ],
        },
        {
            "category": "SPOKEN LANGUAGES",
            "index": "05",
            "skills": ["English (Native)", "French (Fluent)", "Hebrew (Fluent)"],
        },
    ]

    # Certifications, most recent first
    certifications = [
        {
            "title": "Responsive Web Design",
            "issuer": "freeCodeCamp",
            "date": "Aug 2026",
            "description": (
                "Developer Certification representing approximately 300 hours of coursework "
                "covering responsive layouts, Flexbox, Grid, and accessible design."
            ),
            "link": "https://freecodecamp.org/certification/shireldahan/responsive-web-design-v9",
        },
        {
            "title": "HTML Styling with CSS",
            "issuer": "Coddy",
            "date": "Jun 2026",
            "description": (
                "Certificate of completion covering applying CSS to structure and style HTML "
                "documents."
            ),
            "link": "",
        },
        {
            "title": "HTML Fundamentals",
            "issuer": "Coddy",
            "date": "May 2026",
            "description": (
                "Certificate of completion covering core HTML structure, semantics, and markup."
            ),
            "link": "",
        },
    ]

    return render_template("skills.html", skill_groups=skill_groups, certifications=certifications)


@app.route("/projects")
def projects():
    """Projects page, current builds and placeholders for future work."""

    projects_list = [
        {
            "number": "01",
            "title": "Swim with Shirel",
            "description": (
                "A full website for my private swimming lesson business, built and deployed "
                "independently. Handles scheduling information, availability, and contact. "
                "Live on Railway."
            ),
            "tags": ["Python", "Flask", "HTML", "CSS", "Railway"],
            "status": "LIVE",
            "link": "https://swim-with-shirel-production.up.railway.app/",
            "github": "#",
        },
        {
            "number": "02",
            "title": "Portfolio Website",
            "description": (
                "Designed and built with Flask, HTML, and CSS. A personal brand "
                "system featuring a dark green tennis-inspired visual language and editorial layout. "
                "The first real thing I built for myself."
            ),
            "tags": ["Python", "Flask", "HTML", "CSS", "Claude Code"],
            "status": "LIVE",
            "link": "#",
            "github": "https://github.com/shirel2005/portfolio",
        },
        {
            "number": "03",
            "title": "Formula Electric: Electrical Systems",
            "description": (
                "Contributing to the electrical systems of McGill Formula Electric's race car. "
                "Working within a multidisciplinary engineering team using version control, "
                "technical documentation, and collaborative design practices."
            ),
            "tags": ["Electrical Engineering", "Systems Design", "Teamwork"],
            "status": "IN PROGRESS",
            "link": "#",
            "github": "#",
        },
        {
            "number": "04",
            "title": "Coming Soon",
            "description": (
                "A new project is taking shape. This space will be updated as I continue "
                "building through coursework, side exploration, and technical curiosity. "
                "Watch this space."
            ),
            "tags": ["TBD"],
            "status": "UPCOMING",
            "link": "#",
            "github": "#",
        },
        {
            "number": "05",
            "title": "Coming Soon",
            "description": (
                "More is coming. I am actively building technical depth through classes, "
                "collaborative engineering, and the kind of late-night problem-solving "
                "that makes the work feel real."
            ),
            "tags": ["TBD"],
            "status": "UPCOMING",
            "link": "#",
            "github": "#",
        },
    ]

    return render_template("projects.html", projects=projects_list)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Contact page, displays the form on GET, handles submission on POST.

    Flask routes can handle multiple HTTP methods.
    GET = someone visits the page (show the form).
    POST = someone submitted the form (process the data).
    """
    if request.method == "POST":
        # Pull submitted values from the form
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Simple validation, make sure nothing is empty
        if not name or not email or not message:
            flash("Please fill in all fields.", "error")
        else:
            # In a real deployment, you would send an email here using Flask-Mail.
            # For now, we print to the terminal and show a success message.
            print(f"\n📬 New message from {name} ({email}):\n{message}\n")
            flash(
                f"Thank you, {name}. Your message has been received. I will be in touch.",
                "success",
            )
            # Redirect after POST to prevent duplicate form submissions on refresh
            return redirect(url_for("contact"))

    return render_template("contact.html")


# ──────────────────────────────────────────────────────────────────
# ENTRY POINT
# This block only runs if you execute app.py directly.
# It won't run if another program imports this file.
# ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # debug=True: Flask auto-reloads when you save changes. Turn off for production.
    app.run(debug=True)
