import os
from dotenv import load_dotenv

#load_dotenv()  # Load environment variables from a .env file if available

# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/fleetdb")
# JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key_here")
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30 





load_dotenv()  # This loads variables from your .env file into the environment

# Environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/fleetdb")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretjwtkey")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
ALGORITHM = os.getenv("ALGORITHM", "HS256")

