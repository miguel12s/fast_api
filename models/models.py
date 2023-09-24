from sqlalchemy import Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String,Boolean
from sqlalchemy.orm import relationship
from config.db import Base,engine


# class User(Base):
#     __tablename__="users"
#     id=Column(Integer,primary_key=True)
#     id_stage=Column(Integer,nullable=False,unique=True)
#     id_rol=Column()
#     name=Column(String(255),nullable=False)
#     email=Column(String(255),nullable=False,unique=True)
#     password= Column("password",String(255),nullable=False)
#     roles=relationship("Roles",back_populates="user")
#     stages=relationship("Stages",back_populates="user")

# class Programs(Base):
#        __tablename__="programs"
#        id_programa=Column("id_program",Integer,primary_key=True,nullable=False)
#        programa=Column("program",String(120),nullable=False,unique=True)
#        id_facultad=Column(Integer,ForeignKey("faculties.id_facultad"))
#        facultad=relationship("Faculties",back_populates="programs")


# class Roles(Base):
#       __tablename__="roles"
#       roles=Column(String(100),unique=True,nullable=True)
#       id_rol=Column(Integer, ForeignKey("users.id"), primary_key=True)
#       user=relationship("User",back_populates="roles")

# class TypesDocument(Base):
#       __tablename__="type_documents"
#       typeDocument=Column(String(10),unique=True,nullable=True)
#       id_typeDocument=Column(Integer,primary_key=True)

# class Stages(Base):
#       __tablename__="stages"
#       id_stage=Column(Integer,ForeignKey("users.id_stage"), primary_key=True )
#       stage=Column(String(200),unique=True,nullable=False)
#       user=relationship("User",back_populates="stages")
      
   
# class Students(Base):
#        pass

# class Capabilities(Base):
#       __tablename__="capabilities"
#       id_capabilitie=Column(Integer,ForeignKey("clas"))
      
# class Teachers(Base):
#       pass



# class TutoringStages(Base):
#       pass

# class Faculties(Base):
#       __tablename__="faculties"
#       id_facultad=Column(Integer,primary_key=True)
#       facultad=Column(String(255),unique=True,nullable=False)
#       programs=relationship("Programs",back_populates="facultad")

#       def to_dict(self):

#             return {
#                   "id_facultad":self.id_facultad,
#                   "facultad":self.facultad
#             }


# class TutoringSchedule(Base):
#       pass

# class StudentList(Base):
#       pass
# class Subjects(Base):
#        __tablename__="subjects"
#        id_subject=Column(Integer,primary_key=True)
#        subject=Column(String(255),unique=True,nullable=False)




# class Classrooms(Base):
#       pass

# class Locations(Base):
#       __tablename__="locations"
#       id_sede=Column(Integer,primary_key=True)
#       sede=Column(String(100),unique=True)
      
class registroActividad(Base):
    __tablename__="registro_actividad"
    id_registro_actividad=Column(Integer,primary_key=True)
    id_tipo_actividad=Column(Integer,index=True)
    id_usuario=Column(Integer,index=True)
    fecha=Column(String(255),nullable=False)
    hora=Column(String(255),nullable=False)
    ubicacion_actividad=Column(String(255),nullable=False)
    usuario=relationship("usuarios",back_populates="actividad")
class tipoEstado(Base):
    __tablename__="tipoestado"
    id_tipo_estado=Column(Integer,primary_key=True)
    tipo_estado=Column(Integer,nullable=False,unique=True)


class sedes(Base):
    __tablename__="sedes"

    id_sede=Column(Integer,primary_key=True)
    sede=Column(String(255),unique=True)

class programas(Base):
    __tablename__="programas"

    id_programa=Column(Integer,primary_key=True)
    programa=Column(String(255),unique=True,nullable=False)


class facultades(Base):
    __tablename__="facultades"
    id_facultad=Column(Integer,primary_key=True)
    facultad=Column(String(255),unique=True)
    def to_dict(self):

            return {
                  "id_facultad":self.id_facultad,
                  "facultad":self.facultad
            }

class materias(Base):
    __tablename__="materias"

    id_materia=Column(Integer,ForeignKey("horario_tutorias.id_materia"), primary_key=True)
    materia=Column(String(255),unique=True,nullable=False)
    horario=relationship("horario_tutorias",back_populates="materia")




class capacidades(Base):
    __tablename__="capacidades"
    id_capacidad=Column(Integer,primary_key=True)
    capacidad=Column(String(255),unique=True,nullable=False)

class salones(Base):
    __tablename__="salones"
    id_salon=Column(Integer,primary_key=True)
    id_sede=Column(Integer,index=True,nullable=False)
    id_capacidad=Column(Integer,index=True,nullable=False)
    salon=Column(String(255),unique=True,nullable=False)

class campoad(Base):
    __tablename__="campoad"
    id_campo=Column(Integer,primary_key=True)
    campo=Column(String(255),unique=True,nullable=False)

class camposxusuario(Base):
    __tablename__="camposxusuario"
    id_campoxusu=Column(Integer,primary_key=True)
    id_usuario=Column(Integer,unique=True,nullable=False)
    id_campo=Column(Integer,index=True,nullable=False)
    dato=Column(String(255),nullable=False)
    campos=relationship("usuarios",back_populates="campos")


class horario_tutorias(Base):
    __tablename__="horario_tutorias"
    id_tutoria=Column(Integer,primary_key=True)
    id_facultad=Column(Integer,index=True,nullable=False)
    id_programa=Column(Integer,index=True,nullable=False)
    id_materia=Column(Integer,index=True,nullable=False)
    id_salon=Column(Integer,index=True,nullable=False)
    id_usuario=Column(Integer,index=True,nullable=False)
    id_estado_tutoria=Column(Integer,index=True,nullable=False)
    cupos=Column(String(255),nullable=False)
    tema=Column(String(255),nullable=False)
    fecha=Column(String(255),nullable=False)
    hora_inicial=Column(String(255),nullable=False)
    hora_final=Column(String(255),nullable=False)
    horario=relationship("usuarios",back_populates="usuario")
    materia=relationship("materias",back_populates="materia")
    

class lista_estudiantes(Base):
      __tablename__="lista_estudiantes"
      id_lista=Column(Integer,primary_key=True)
      id_tutoria=Column(Integer,index=True,nullable=False)
      id_usuario=Column(Integer,unique=True,nullable=False)
      comentario=Column(String(255),nullable=False)
      asistencia=Column(Boolean,nullable=False,default=False)
      usuario=relationship("usuarios",back_populates="lista")

class Roles(Base):
      __tablename__="roles"
      id_rol=Column(Integer, primary_key=True)
      rol=Column(String(255),unique=True,nullable=True)
      usuarios=relationship("usuarios",back_populates="roles")

class tipos_documento(Base):
       __tablename__="tipos_documento"
       id_tipo_documento=Column(Integer,primary_key=True)
       tipo_documento=Column(String(255),unique=True,nullable=True)

class tipoxestado(Base):
    __tablename__="tipoxestado"
    id_tipoxestado=Column(Integer,primary_key=True)
    id_tipoestado=Column(Integer,index=True,nullable=False)
    estado=Column(String(255),nullable=False)
    usuario=relationship("usuarios",back_populates="estado")

class tipo_registro_actividad(Base):
    __tablename__="tipo_registro_actividad"
    id_tipo_actividad=Column(Integer,primary_key=True)
    tipo_actividad=Column(String(255),nullable=False)

class usuarios(Base):
    __tablename__="usuarios"
    id_usuario =Column(Integer,ForeignKey("horario_tutorias.id_usuario"),ForeignKey("registro_actividad.id_usuario"),ForeignKey("lista_estudiantes.id_usuario"),
                       ForeignKey("camposxusuario.id_usuario"), primary_key=True)
    id_rol=Column(Integer,ForeignKey("roles.id_rol"),unique=True, nullable=False)
    id_estado=Column(Integer,ForeignKey("tipoxestado.id_tipoxestado"),unique=True, nullable=False)
    nombres=Column(String(255),nullable=False)
    apellidos=Column(String(255),nullable=False)
    tipo_documento =Column(String(255),nullable=False)
    numero_documento=Column(String(255),unique=True,nullable=False)
    celular=Column(String(255),nullable=False)
    facultad=Column(String(255),nullable=False)
    foto =Column(String(255),nullable=False)
    correo=Column(String(255),unique=True,nullable=False) 
    contraseña =Column(String(255),nullable=False)
    usuario=relationship("horario_tutorias",back_populates="horario")
    lista=relationship("lista_estudiantes",back_populates="lista")
    actividad=relationship("registro_actividad",back_populates="actividad")
    campos=relationship("camposxusuario",back_populates="campos")
    roles=relationship("roles",back_populates="usuario")
    estado=relationship("tipoxestado",back_populates="usuario")





Base.metadata.create_all(engine)





