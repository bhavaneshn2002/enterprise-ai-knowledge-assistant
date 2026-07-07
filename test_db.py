from app.database.connection import engine

try:
    connection = engine.connect()
    print("✅ Database connected successfully!")

    connection.close()
    print("✅ Database connection closed.")

except Exception as e:
    print("❌ Database connection failed!")
    print(e)