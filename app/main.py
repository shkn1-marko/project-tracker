from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .database import SessionLocal, init_db
from .models import Entry, EntryType


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):
    db = SessionLocal()
    right_now = db.query(Entry).filter(Entry.type == EntryType.right_now).all()
    goals = db.query(Entry).filter(Entry.type == EntryType.goal).all()
    projects = db.query(Entry).filter(Entry.type == EntryType.project).all()
    db.close()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "right_now": right_now,
            "goals": goals,
            "projects": projects,
        },
    )
