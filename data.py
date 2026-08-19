from app.database import SessionLocal, init_db
from app.models import Entry, EntryType, Status

init_db()
db = SessionLocal()

db.add_all(
    [
        Entry(
            type=EntryType.right_now,
            title="Izrađujem web-stranicu koristeći FastAPI",
            description="Koristim Python, FastAPI, Jinja za izradu stranice. Za posluživanje stranice koristim VPS, Nginx, Systemd",
            github_url = "https://github.com/shkn1-marko/project-tracker",
        ),
        Entry(type=EntryType.goal,
              title="PyTorch / Tensorflow",
              description="Želim saznati više o ML / AI bibliotekama izradom vlastitih projekata",
        ),
        Entry(type=EntryType.goal,
              title="Docker / Kubernetes",
              description="Želim saznati što je to Docker / Kubernetes",
        ),
        Entry(
            type=EntryType.project,
            title="Web-stranica za praćenje projekata",
            description="Originalna ideja ovog projekta je stvaranje jedinstvenog pregleda u moj portfolio, koja na jednom mjestu prikazuje informacije koje inače postoje na više mjesta kao što su GitHub profil, životopis, web-stranice projekta. Cilj koji želim ostvariti je bolje predstavljnje potencijalnim poslodavcima. Dodatno želim obnoviti praksu programiranja u Python-u i savladati izradu manjih web-stranica.",
            github_url="https://github.com/shkn1-marko/project-tracker",
            webpage_url="https://marko-palameta.com.hr",
            status=Status.yellow,
        ),
        Entry(
            type=EntryType.project,
            title="Pokretač video igara",
            description="U slobodno vrijeme izrađujem vlastiti 'game engine'.",
            status=Status.yellow,
        ),
        Entry(
            type=EntryType.project,
            title="Video igra (Online/Multiplayer/Server-Client)",
            description="Izradio sam video igru (C++), koju igraju dva igrača, na dva računala, pomoću servera (Go).",
            status=Status.green,
        ),
    ]
)
db.commit()
db.close()
