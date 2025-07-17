import hashlib
from dna_generator import generate_dna

def hash_dna(dna: str) -> str:
    return hashlib.sha256(dna.encode()).hexdigest()

def hashed_dna() -> str:
    dna = generate_dna()
    hashed = hash_dna(dna)
    return hashed
