from database import Base, engine
from models import Drug

print("Creating database and tables...")
Base.metadata.create_all(bind=engine)
print("✅ Done. 'drugs.db' with 'drugs' table created.")
