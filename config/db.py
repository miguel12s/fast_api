from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:@localhost:3306/bd")
sessionLocal=sessionmaker(engine)
Base=declarative_base()
