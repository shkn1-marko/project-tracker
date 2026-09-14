from app.database import SessionLocal, init_db
from app.models import Entry, EntryType, Status

init_db()
db = SessionLocal()

db.query(Entry).delete()
db.commit()

db.add_all(
    [
        Entry(
            type=EntryType.right_now,
            title="Izrađujem mobilnu aplikaciju",
            description="Istražujem kako napraviti [Android] mobilnu aplikaciju.",
        ),
        Entry(
            type=EntryType.goal,
            title="YouTube video",
            description="Želim napraviti kratki YouTube video koji predstavlja jedan od mojih projekata.",
        ),
        Entry(
            type=EntryType.project,
            title="Alat za auto-deploy : go-deploy",
            description="Volim programirati u Go(u). Ovaj alat omogućuje automatsko podizanje mojih projekata koji se nalaze na serveru. Kada se dogodi promjena na mojem GitHub projektu, go-deploy prima poruku od GitHub(a), izvršava skripte za podizanje projekta i obavještava o uspjehu/neuspjehu putem elektroničke pošte.",
            github_url="https://github.com/shkn1-marko/go-deploy",
            status=Status.green,
        ),
        Entry(
            type=EntryType.project,
            title="C++ [Multiplayer] Pong",
            description="Volim programirati u C++(u). Ovaj projekt izradio sam kao dokaz tehničkih sposobnosti. Projekt se sastoji od klijenta, servera i zajedničkog protokola za komunikaciju. Klijent koristi OpenGL za crtanje video igre. Komunikacija je ostvarena putem biblioteka operacijskog sustava: <winsock2.h> i <sys/socket.h>. Server omogućuje igru na dva računala putem internetske mreže.",
            github_url="https://github.com/shkn1-marko/pong",
            status=Status.green,
        ),
        Entry(
            type=EntryType.project,
            title="Osobna web stranica",
            description="Ideja ove web stranice je izrada jednostavnog pregleda svih mojih projekata, ciljeva i trenutnih zadataka na jednom mjestu. Cilj ovog projekta je pojednostaviti upoznavanje s potencijalnim poslodavcima. Dodatno, želio sam priliku da izradim web stranicu, programiram u Python-u i izradim jednostavnu bazu podataka (SQLite).",
            github_url="https://github.com/shkn1-marko/project-tracker",
            status=Status.green,
        ),
    ]
)
db.commit()
db.close()
