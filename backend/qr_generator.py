
import qrcode
from hash_dna import generate_dna, hash_dna

def generate_qr(data: str, filename="medicine_qr.png"):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR saved as {filename}")

if __name__ == "__main__":
    dna = generate_dna()
    hash_value = hash_dna(dna)
    print(f"DNA: {dna}")
    print(f"Hash: {hash_value}")
    generate_qr(hash_value)
