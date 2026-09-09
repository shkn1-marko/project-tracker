from app.database import SessionLocal, init_db
from app.models import Entry, EntryType, Status

init_db()
db = SessionLocal()

db.add_all(
    [
        Entry(
            type=EntryType.right_now,
            title="Gradim osnovni program (Go)",
            description="Trenutno pišem osnove programa koji će postati moj alat za administraciju servera. Radim na osnovnim naredbama (make, list, remove, start, stop).",
            github_url="https://github.com/shkn1-marko/go-deploy",
        ),
        Entry(
            type=EntryType.goal,
            title="Rad u struci",
            description="Želim pronaći posao u struci.",
        ),
        Entry(
            type=EntryType.project,
            title="Alat za administraciju servera",
            description="Trenutno planiram izradu alata koji bi mi olakšao upravljanje serverom. Želio bih automatizirati ažuriranje i pokretanje projekata koji se nalaze na serveru. Alat planiram izraditi u programskom jeziku Go.",
            github_url="https://github.com/shkn1-marko/go-deploy",
            status=Status.yellow,
        ),
        Entry(
            type=EntryType.project,
            title="Pong",
            description="U slobodno vrijeme izrađujem video igre. Pong je jednostavna igra pomoću koje želim naučiti više o programiranju u C++-u i OpenGL-u. Želim naučiti kako izrađivati veće sustave u C++-u. Također želim naučiti više o mrežnom programiranju i savladati korištenje mrežnog protokola UDP.",
            github_url="https://github.com/shkn1-marko/pong",
            status=Status.green,
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
