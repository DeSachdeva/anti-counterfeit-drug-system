# qr_generator.py
import qrcode
import json
import os
from hash_dna import generate_dna, hash_dna

def generate_qr(qr_data: dict, id: int):
    qr = qrcode.make(json.dumps(qr_data))
    qr_dir = "qr_codes"
    os.makedirs(qr_dir, exist_ok=True)
    qr_path = os.path.join(qr_dir, f"{id}_qr.png")
    qr.save(qr_path)
    return

if __name__ == "__main__":
    dna = generate_dna()
    hash_value = hash_dna(dna)

    # Collect all details to include in QR
    medicine_data = {
        "id": "081782",
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