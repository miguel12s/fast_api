from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:@localhost:3306/ejemplo")
sessionLocal=sessionmaker(bind=engine)
Base=declarative_base()
conn=engine.connect()

def get_db() -> Session:
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()