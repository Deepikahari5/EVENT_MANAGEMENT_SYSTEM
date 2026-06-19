from sqlalchemy import create_engine
from sqlalchemy import text

DATABASE_URL = (
    "mysql+pymysql://root:Deepikahari%4005@localhost:3306/event_management_db"
)

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Database Connected Successfully!")
except Exception as e:
    print("❌ Error:", e)