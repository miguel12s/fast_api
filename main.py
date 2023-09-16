from fastapi import FastAPI
from routes.user import user_router
from routes.admin import admin
app = FastAPI()
app.include_router(user_router)
app.include_router(admin)