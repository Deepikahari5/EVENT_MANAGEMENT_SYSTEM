from sqlalchemy import create_engine

DATABASE_URL = (
    "mysql+pymysql://root:Deepikahari%4005@localhost:3306/event_management_db"
)

connectable = create_engine(
    DATABASE_URL
)