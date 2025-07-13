from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Aushadhi Rakshak")

origins = ["https://aushadhi-rakshak.vercel.app/"
           #add frontend deployment link here
        ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Database ---
from .database import Base, engine
Base.metadata.create_all(bind=engine)

# --- Routes ---
from . import drugs
app.include_router(drugs.router, prefix="/drugs", tags=["Drugs"])

@app.get("/")
def root():
    return {"message": "Drug Verification System using DNA + FastAPI"}