from app.database.database import SessionLocal
from app.models.role import Role

db = SessionLocal()

roles = [
    {"name": "Admin"},
    {"name": "Organizer"},
    {"name": "Participant"}
]

for role in roles:
    existing = db.query(Role).filter(Role.name == role["name"]).first()

    if not existing:
        db.add(Role(**role))

db.commit()

print("Roles inserted successfully")