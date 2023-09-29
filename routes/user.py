from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from schemas.User import User as UserSchema
from schemas.Program import Program as ProgramSchema

user_router = APIRouter()

# @user_router.get('/users')
# def get_users():
#     with Session(engine) as session:
#         users = session.execute(select(Usuarios))
#         user_list = [{"id_usuario": user.id, "name": user.name, "email": user.email} for user in users]
#         return user_list

# @user_router.post('/users')
# def create_user(user: UserSchema):
#     with Session(engine) as session:
#         new_user = Usuarios(name=user.name, email=user.email, password=user.password)
#         session.add(new_user)
#         session.commit()
#         return {"id": new_user.id, "name": new_user.name, "email": new_user.email}

# @user_router.get('/users/{user_id}')
# def get_user(user_id: int):
#     with Session(engine) as session:
#         user = session.execute(select(Usuarios).where(Usuarios.id == user_id)).first()
#         if user:
#             return {"id": user.id, "name": user.name, "email": user.email}
#         raise HTTPException(status_code=404, detail="User not found")

# @user_router.post('/programs')
# def insert_program(program: ProgramSchema):
#     with Session(engine) as session:
#         new_program = Programa(id_program=program.id, programa=program.program)
#         try:
#             session.execute(insert(Programa).values(new_program))
#             session.commit()
#             return new_program
#         except Exception as e:
#             print(e)
#             raise HTTPException(status_code=400, detail="Program already exists")

