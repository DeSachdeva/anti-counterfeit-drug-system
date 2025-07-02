import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import datetime

class dna_sequence(BaseModel):
    medicine_id: str
    batch_id: str
    date_of_manufacturing: str
    date_of_expiring: str
    sequence: str

app = FastAPI()


