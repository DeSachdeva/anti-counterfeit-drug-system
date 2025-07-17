from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routes import drugs

app = FastAPI(title="Aushadhi Rakshak")


origins = [
    "http://127.0.0.1:3000",
    "https://aushadhi-rakshak.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(drugs.router, prefix="/drugs", tags=["Drugs"])

@app.get("/")
def root():
    return {"message": "Drug Verification System using DNA + FastAPI"}
