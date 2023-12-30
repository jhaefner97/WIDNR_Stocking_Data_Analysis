import googlemaps
import os
import sqlalchemy

from dotenv import load_dotenv
from enum import Enum
from pathlib import Path

load_dotenv()

class Paths:

    def __init__(self) -> None:
        self.project_dir = Path.cwd()

        self.databases_dir = self.project_dir / "Databases"
        self.stocking_database = self.databases_dir / os.getenv("stocking_database")

class Utils(Enum):
    paths = Paths()
    api_key = os.getenv("google_maps_key")
    db_engine = sqlalchemy.create_engine(f"sqlite:///{paths.stocking_database}")
    google_client  = googlemaps.Client(key=api_key)


