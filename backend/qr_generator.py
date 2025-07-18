# qr_generator.py
import qrcode
import json
import os
from hash_dna import generate_dna, hash_dna

def generate_qr(qr_data: dict, id: int):
    import io, base64
    qr = qrcode.make(json.dumps(qr_data))
    import io, base64
    buf = io.BytesIO()
    qr.save(buf, format='PNG')
    img_bytes = buf.getvalue()
    img_b64 = base64.b64encode(img_bytes).decode('utf-8')
    return img_b64

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