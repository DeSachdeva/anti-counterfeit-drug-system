import random

def generate_dna(length=20):
    return ''.join(random.choices("ATCG", k=length))

if __name__ == "__main__":
    dna = generate_dna()
    print("Generated DNA:", dna)
