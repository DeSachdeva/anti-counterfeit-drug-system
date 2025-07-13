
import hashlib
from dna_generator import generate_dna

def hash_dna(dna: str) -> str:
    return hashlib.sha256(dna.encode()).hexdigest()

if __name__ == "__main__":
    dna = generate_dna()
    hashed = hash_dna(dna)
    print(f"DNA: {dna}")
    print(f"Hash: {hashed}")
