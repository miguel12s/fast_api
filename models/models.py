from sqlalchemy import Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from config.db import Base,engine


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    id_stage=Column(Integer,nullable=False,unique=True)
    name=Column(String(255),nullable=False)
    email=Column(String(255),nullable=False,unique=True)
    password= Column("password",String(255),nullable=False)
    roles=relationship("Roles",back_populates="user")
    stages=relationship("Stages",back_populates="user")

class Programs(Base):
       __tablename__="programs"
       id_programa=Column("id_program",Integer,primary_key=True,nullable=False)
       programa=Column("program",String(120),nullable=False,unique=True)
       id_facultad=Column(Integer,ForeignKey("faculties.id_facultad"))
       facultad=relationship("Faculties",back_populates="programs")


class Roles(Base):
      __tablename__="roles"
      roles=Column(String(100),unique=True,nullable=True)
      id_rol=Column(Integer, ForeignKey("users.id"), primary_key=True)
      user=relationship("User",back_populates="roles")

class TypesDocument(Base):
      __tablename__="type_documents"
      typeDocument=Column(String(10),unique=True,nullable=True)
      id_typeDocument=Column(Integer,primary_key=True)

class Stages(Base):
      __tablename__="stages"
      id_stage=Column(Integer,ForeignKey("users.id_stage"), primary_key=True )
      stage=Column(String(200),unique=True,nullable=False)
      user=relationship("User",back_populates="stages")
      

# class Students(Base):
#        pass

# class Capabilities(Base):
#       __tablename__="capabilities"
#       id_capabilitie=Column(Integer,ForeignKey("clas"))
      
# class Teachers(Base):
#       pass



# class TutoringStages(Base):
#       pass

class Faculties(Base):
      __tablename__="faculties"
      id_facultad=Column(Integer,primary_key=True)
      facultad=Column(String(255),unique=True,nullable=False)
      programs=relationship("Programs",back_populates="facultad")

      def to_dict(self):

            return {
                  "id_facultad":self.id_facultad,
                  "facultad":self.facultad
            }


# class TutoringSchedule(Base):
#       pass

# class StudentList(Base):
#       pass
class Subjects(Base):
       __tablename__="subjects"
       id_subject=Column(Integer,primary_key=True)
       subject=Column(String(255),unique=True,nullable=False)




# class Classrooms(Base):
#       pass

class Locations(Base):
      __tablename__="locations"
      id_sede=Column(Integer,primary_key=True)
      sede=Column(String(100),unique=True)
      







Base.metadata.create_all(engine)





