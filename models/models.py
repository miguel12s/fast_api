from sqlalchemy import Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String,Boolean
from sqlalchemy.orm import relationship
from config.db import Base,engine
from sqlalchemy.orm import declarative_base

Base=declarative_base()

    # usuario=relationship("usuarios",back_populates="actividad")
class TipoEstado(Base):
    __tablename__="tipoestado"
    id_tipo_estado=Column(Integer,primary_key=True)
    tipo_estado=Column(Integer,nullable=False,unique=True)
    tipoxestado=relationship("Tipoxestado",back_populates="tipoestado")


class Sedes(Base):
    __tablename__="sedes"

    id_sede=Column(Integer,primary_key=True)
    sede=Column(String(255),unique=True)
    salones=relationship("Salones",back_populates="sedes")


class FacultadXPrograma(Base):
    __tablename__ = "facultadxprograma"
    id_fxp = Column(Integer, primary_key=True)
    id_facultad = Column(Integer, ForeignKey("facultades.id_facultad"), index=True, nullable=False)
    id_programa = Column(Integer, ForeignKey("programas.id_programa"), index=True, nullable=False)

    facultad = relationship("Facultad", back_populates="programas_intermedia")
    programa = relationship("Programa", back_populates="facultades_intermedia")
    horario_tutoria=relationship("Horario_tutorias",back_populates="facultadxprograma")
class Programa(Base):
    __tablename__ = "programas"

    id_programa = Column(Integer, primary_key=True)
    programa = Column(String(255), unique=True, nullable=False)

    facultades_intermedia = relationship("FacultadXPrograma", back_populates="programa")

class Facultad(Base):
    __tablename__ = "facultades"
    id_facultad = Column(Integer, primary_key=True)
    facultad = Column(String(255), unique=True)

    programas_intermedia = relationship("FacultadXPrograma", back_populates="facultad")

    def to_dict(self):
        return {
            "id_facultad": self.id_facultad,
            "facultad": self.facultad
        }

class Materias(Base):
    __tablename__="materias"

    id_materia=Column(Integer, primary_key=True)
    materia=Column(String(255),unique=True,nullable=False)
    moduloxrol=relationship("Moduloxrol",back_populates="materias")




class Capacidades(Base):
    __tablename__="capacidades"
    id_capacidad=Column(Integer,primary_key=True)
    capacidad=Column(String(255),unique=True,nullable=False)
    salones=relationship("Salones",back_populates="capacidades")

class Salones(Base):
    __tablename__="salones"
    id_salon=Column(Integer,primary_key=True)
    id_sede=Column(Integer,ForeignKey("sedes.id_sede") ,index=True, nullable=False)
    id_capacidad=Column(Integer,ForeignKey("capacidades.id_capacidad"),index=True,nullable=False)
    salon=Column(String(255),unique=True,nullable=False)
    sedes=relationship("Sedes",back_populates="salones")
    capacidades=relationship("Capacidades",back_populates="salones")
    horario_tutoria=relationship("Horario_tutorias",back_populates="salones")

class Campoad(Base):
    __tablename__="campoad"
    id_campo=Column(Integer,primary_key=True)
    campo=Column(String(255),unique=True,nullable=False)    
    camposxusuario=relationship("Camposxusuario",back_populates="campoad")



class Camposxusuario(Base):
    __tablename__="camposxusuario"
    id_campoxusu=Column(Integer,primary_key=True)
    id_usuario=Column(Integer,ForeignKey("usuarios.id_usuario"), unique=True,nullable=False)
    id_campo=Column(Integer,ForeignKey("campoad.id_campo"),   index=True,nullable=False)
    dato=Column(String(255),nullable=False)
    campoad=relationship("Campoad",back_populates="camposxusuario")
    usuario=relationship("Usuarios",back_populates="camposxusario")


class Horario_tutorias(Base):
    __tablename__="horario_tutorias"
    id_tutoria=Column(Integer,primary_key=True)
    id_fxp=Column(Integer,ForeignKey("facultadxprograma.id_fxp"), index=True,nullable=False)
    id_mxr=Column(Integer,ForeignKey("moduloxrol.id_mxr"), index=True,nullable=False)
    id_salon=Column(Integer,ForeignKey("salones.id_salon"), index=True,nullable=False)
    id_usuario=Column(Integer,ForeignKey("usuarios.id_usuario"), index=True,nullable=False)
    id_estado_tutoria=Column(Integer,ForeignKey("tipoxestado.id_tipoxestado"), index=True,nullable=False)
    cupos=Column(String(255),nullable=False)
    tema=Column(String(255),nullable=False)
    fecha=Column(String(255),nullable=False)
    hora_inicial=Column(String(255),nullable=False)
    hora_final=Column(String(255),nullable=False)
    facultadxprograma=relationship("FacultadxPrograma",back_populates="id_fxp")
    salones=relationship("Salones",back_populates="horario_tutoria")
    moduloxrol=relationship("Moduloxrol",back_populates="horario_tutorias")
    lista_estudiante=relationship("Lista_estudiantes",back_populates="horario_tutoria")
    usuario=relationship("Usuarios",back_populates="horario_tutorias")
    tipoxestado=relationship("Tipoxestado",back_populates="horario_tutorias")

class Usuarios(Base):
    __tablename__="usuarios"
    id_usuario=Column(Integer,primary_key=True)
    id_rol=Column(Integer,ForeignKey("roles.id_rol"),unique=True, nullable=False)
    id_estado=Column(Integer, ForeignKey("tipoxestado.id_tipoxestado"), unique=True, nullable=False)
    nombres=Column(String(255),nullable=False)
    apellidos=Column(String(255),nullable=False)
    id_tipo_documento=Column(Integer,ForeignKey("tipos_documento.id_tipo_documento"),  nullable=False)
    numero_documento=Column(String(255),unique=True,nullable=False)
    celular=Column(String(255),nullable=False)
    facultad=Column(String(255),nullable=False)
    foto =Column(String(255),nullable=False)
    correo=Column(String(255),unique=True,nullable=False) 
    contraseña =Column(String(255),nullable=False)
    tipo_documento=relationship("Tipos_documento",back_populates="usuarios")
    registro_actividad=relationship("RegistroActividad",back_populates="usuario")
    roles=relationship("Roles",back_populates="usuarios")
    camposxusuario=relationship("Usuarios",back_populates="usuario")
    lista_estudiante=relationship("Lista_estudiantes",back_populates="usuario")
    horario_tutorias=relationship("Horario_tutorias",back_populates="usuario")
    tipoxestado=relationship("Usuarios",back_populates="usuario")
    # usuario=relationship("horario_tutorias",back_populates="horario")
    # lista=relationship("lista_estudiantes",back_populates="lista")
    # actividad=relationship("registro_actividad",back_populates="actividad")
    # campos=relationship("camposxusuario",back_populates="campos")
    # roles=relationship("roles",back_populates="usuario")
    # estado=relationship("tipoxestado",back_populates="usuario")
   

class Lista_estudiantes(Base):
      __tablename__="lista_estudiantes"
      id_lista=Column(Integer,primary_key=True)
      id_tutoria=Column(Integer,ForeignKey("horario_tutorias.id_tutoria"),   index=True,nullable=False)
      id_usuario=Column(Integer,ForeignKey("usuarios.id_usuario"),unique=True,nullable=False)
      comentario=Column(String(255),nullable=False)
      asistencia=Column(Boolean,nullable=False,default=False)
      
      usuario=relationship("Usuarios",back_populates="lista_estudiante")
      horario_tutoria=relationship("Horario_tutorias",back_populates="lista_estudiante")

class Roles(Base):
      __tablename__="roles"
      id_rol=Column(Integer, primary_key=True)
      rol=Column(String(255),unique=True,nullable=True)
      moduloxrol=relationship("Moduloxrol",back_populates="roles")
      usuarios=relationship("Usuarios",back_populates="roles")

class Tipos_documento(Base):
       __tablename__="tipos_documento"
       id_tipo_documento=Column(Integer,primary_key=True)
       tipo_documento=Column(String(255),unique=True,nullable=True)
       usuarios=relationship("Usuarios",back_populates="tipo_documento")

class Tipoxestado(Base):
    __tablename__="tipoxestado"
    id_tipoxestado=Column(Integer,primary_key=True)
    id_tipoestado=Column(Integer,ForeignKey("tipoestado.id_tipo_estado"),index=True, nullable=False)
    estado=Column(String(255),nullable=False)
    tipoestado=relationship("TipoEstado",back_populates="tipoxestado")
    tipoxestado=relationship("Horario_tutorias",back_populates="tipoxestado")
    usuario=relationship("Tipoxestado",back_populates="tipoxestado")

class Tipo_registro_actividad(Base):
    __tablename__="tipo_registro_actividad"
    id_tipo_actividad=Column(Integer,primary_key=True)
    tipo_actividad=Column(String(255),nullable=False)
    registro_actividad=relationship("RegistroActividad",back_populates="tipo_registro_actividad")

class RegistroActividad(Base):
    __tablename__="registro_actividad"
    id_registro_actividad=Column(Integer,primary_key=True)
    id_tipo_actividad=Column(Integer,ForeignKey("tipo_registro_actividad.id_tipo_actividad"), index=True)
    id_usuario=Column(Integer,ForeignKey("usuarios.id_usuario"),index=True)
    fecha=Column(String(255),nullable=False)
    hora=Column(String(255),nullable=False)
    ubicacion_actividad=Column(String(255),nullable=False)
    tipo_registro_actividad=relationship("Tipo_registro_actividad",back_populates="registro_actividad")
    usuario=relationship("Usuarios",back_populates="registro_actividad")



class Moduloxrol(Base):
     __tablename__="moduloxrol"
     id_mxr=Column(Integer,primary_key=True)
     id_materia=Column(Integer,ForeignKey("materias.id_materia"),index=True,nullable=False)
     id_rol=Column(Integer,ForeignKey("roles.id_rol"), index=True,nullable=False)
     materias=relationship("Materias",back_populates="moduloxrol")
     roles=relationship("Roles",back_populates="moduloxrol")
     horario_tutorias=relationship("Horario_tutorias",back_populates="moduloxrol")

Base.metadata.create_all(engine)
