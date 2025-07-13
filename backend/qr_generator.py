# qr_generator.py
import qrcode
import json
from hash_dna import generate_dna, hash_dna

def generate_qr(data: dict, filename="medicine_qr.png"):
    qr_data = json.dumps(data)
    img = qrcode.make(qr_data)
    img.save(filename)
    print(f"QR with metadata saved as {filename}")

if __name__ == "__main__":
    dna = generate_dna()
    hash_value = hash_dna(dna)

    # Collect all details to include in QR
    medicine_data = {
        "name": "Paracetamol 500mg",
        "drug": "Paracetamol",
        "batch_id": "BATCH12345",
        "manufacturer": "XYZ Pharma Pvt Ltd",
        "mfg_date": "2024-07-01",
        "exp_date": "2026-07-01",
        "hash": hash_value
    }

    print("Data to encode in QR:\n", json.dumps(medicine_data, indent=2))
    generate_qr(medicine_data)
