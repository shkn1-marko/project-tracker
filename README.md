# project-tracker

My personal website, and my first project. I built it to answer one question: how do I present myself as a software engineer in a way that's quick to read? Instead of a static CV, the site is a single page showing what I'm working on right now, what I want to learn next, and the projects I've built, each with a short description and links to the code.

**Live at [marko-palameta.com.hr](https://marko-palameta.com.hr/)** (in Croatian).

## What's on the page

- **Header**: name, degree, location, and contact details.
- **Right now (Trenutno)**: what I'm currently working on.
- **Goals (Ciljevi)**: things I want to learn or do next.
- **Projects (Projekti)**: finished and ongoing projects, each with a red / yellow / green status dot.

Click any entry to expand it and see its description and links to GitHub, YouTube or a web page.

## How it's built

- **Backend**: Python with FastAPI, serving one server-rendered page through Jinja2 templates.
- **Data**: every entry is a row in a SQLite database, accessed with SQLAlchemy. Entries have a type (right now, goal, or project), an optional status, and optional links. To update the site, I edit [`data.py`](data.py) and run it to reset the database.
- **Frontend**: hand-written HTML and CSS with no framework, in a dark theme. On mobile, the layout drops to a single column. A small vanilla JavaScript file expands the cards, and only builds each card's details the first time it's opened.

## Running locally

```bash
pip install -r requirements.txt
python data.py
uvicorn app.main:app --reload
```
