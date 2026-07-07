from app.database.connection import engine
from app.database.base import Base

# Import all models here
from app.models.user import User

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("✅ Database tables created successfully!")