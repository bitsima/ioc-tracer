from dotenv import load_dotenv

import os

load_dotenv()  # Load variables from .env file

db_username = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

DATABASE_URL = (
    f"postgresql+psycopg2://{db_username}:{db_password}@ioc_database:5432/{db_name}"
)

virustotal_api_key = os.getenv("VIRUSTOTAL_API_KEY")

db_init_repo = os.getenv("DATABASE_INIT_REPO")
