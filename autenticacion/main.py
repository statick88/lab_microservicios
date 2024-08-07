from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Base
from database.database import Base, engine
from Routes.login.login import router as login_router

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Microservicio Autenticacion"}

app.include_router(login_router)
