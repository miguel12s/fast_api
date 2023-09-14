from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base,engine

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    email=Column(String(255),nullable=False,unique=True)
    password= Column("password",String(255),nullable=False)


class Programs(Base):
       __tablename__="programs"
       id_programa=Column("id_program",Integer,primary_key=True,nullable=False)
       programa=Column("programa",String(120),nullable=False,unique=True)


class Students(Base):
       pass

class Capabilities(Base):
      pass
      
class Teachers(Base):
      pass

class Stages(Base):
      pass

class TutoringStages(Base):
      pass

class Faculties(Base):
      pass

class TutoringSchedule(Base):
      pass

class StudentList(Base):
      pass
class Subjects(Base):
       pass

class Roles(Base):
      pass

class Classrooms(Base):
      pass

class Locations(Base):
      pass

class typesDocument(Base):
      pass







 



Base.metadata.create_all(engine)





