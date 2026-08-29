from app.database import SessionLocal, init_db
from app.models import Entry, EntryType, Status

init_db()
db = SessionLocal()

db.add_all(
    [
        Entry(
            type=EntryType.right_now,
            title="Izrađujem igru 'Pong' pomoću OpenGL-a",
            description="Izrađujem osnovno sučelje za igru Pong, koristim C++ i OpenGL.",
            github_url="https://github.com/shkn1-marko/pong",
        ),
        Entry(
            type=EntryType.goal,
            title="Go",
            description="Želim ponovo raditi u Go programskom jeziku.",
        ),
        Entry(
            type=EntryType.goal,
            title="AI/ML",
            description="Želim dodati u svoj portfolio jedan projekt koji koristi AI/ML.",
        ),
        Entry(
            type=EntryType.project,
            title="Pong",
            description="U slobodno vrijeme izrađujem video igre. Pong je jednostavna igra pomoću koje želim naučiti više o programiranju u C++-u i OpenGL-u. Želim naučiti kako izrađivati veće sustave u C++-u.",
            github_url="https://github.com/shkn1-marko/pong",
            status=Status.yellow,
        ),
        Entry(
            type=EntryType.project,
            title="Web-stranica za praćenje projekata",
            description="Prilikom prijave za poslove suočio sam se sa jedinstvenim problemom. Kako potencijalnom poslodavcu najbolje prestaviti svoj portfolio. Došao sam na ideju da stvorim jedinstveni pogled koji spaja podatke koji se inače nalaze u mom životopisu, na GitHub-u i na web-stranicama mojih projekata. Podatci su podjeljeni u tri kategorije, stvari na kojima upravo radim, dugoročni ciljevi i popis završenih (zeleno) i projekata koji su u izradi (žuto).",
            github_url="https://github.com/shkn1-marko/project-tracker",
            status=Status.green,
        ),
    ]
)
db.commit()
db.close()
