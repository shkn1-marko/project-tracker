from app.database import SessionLocal, init_db
from app.models import Entry, EntryType, Status

init_db()
db = SessionLocal()

db.add_all(
    [
        Entry(
            type=EntryType.right_now, title="Izrađujem web-stranicu koristeći FastAPI"
        ),
        Entry(type=EntryType.goal, title="PyTorch / Tensorflow"),
        Entry(type=EntryType.goal, title="Docker / Kubernetes"),
        Entry(
            type=EntryType.project,
            title="Web-stranica za praćenje projekata",
            status=Status.yellow,
        ),
        Entry(
            type=EntryType.project,
            title="Pokretač video igara",
            status=Status.yellow,
        ),
        Entry(
            type=EntryType.project,
            title="Video igra (Online/Multiplayer/Server-Client)",
            status=Status.green,
        ),
    ]
)
db.commit()
db.close()
