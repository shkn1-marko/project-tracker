from app.database import SessionLocal, init_db
from app.models import Entry, EntryType, Status

init_db()
db = SessionLocal()

db.add_all(
    [
        Entry(
            type=EntryType.right_now,
            title="Izrađujem web-stranicu koristeći FastAPI",
            description="Za izradu stranice koristim Python, FastAPI, Jinja. Stranicu poslužujem na domeni marko-palameta.com.hr uz pomoć VPS, Nginx, Systemd.",
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
            description="Prilikom prijave za poslove suočio sam se sa jedinstvenim problemom. Kako potencijalnom poslodavcu najbolje prestaviti svoj portfolio. Došao sam na ideju da stvorim jedinstveni pogled koji spaja podatke koji se inače nalaze u mom životopisu, na GitHub-u i na web-stranicama mojih projekata. Podatci su podjeljeni u tri kategorije, stvari na kojima upravo radim, dugoročni ciljevi i popis završenih (zeleno) i projekata koji su u izradi (žuto).",
            github_url="https://github.com/shkn1-marko/project-tracker",
            status=Status.green,
        ),
        Entry(
            type=EntryType.project,
            title="Pokretač video igara",
            description="U slobodno vrijeme izrađujem vlastiti pokretač video igara (C++).",
            status=Status.yellow,
        ),
        Entry(
            type=EntryType.project,
            title="Video igra (Online/Multiplayer/Server-Client)",
            description="Izradio sam igru (C++) za dva igrača. Napisao sam server (Go) koji omogućuje igračima da razmjenjuju poteze putem interneta.",
            status=Status.green,
        ),
    ]
)
db.commit()
db.close()
