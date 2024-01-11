import googlemaps
import os
import sqlalchemy
import sqlite3

from dotenv import load_dotenv
from enum import Enum
from pathlib import Path

load_dotenv()

class Paths:

    def __init__(self) -> None:
        self.project_dir = Path.cwd()

        self.databases_dir = self.project_dir / "Databases"
        self.sql_backup_dir = self.databases_dir / "Backups"
        self.stocking_database = self.databases_dir / os.getenv("stocking_database")

class Utils(Enum):
    paths = Paths()
    api_key = os.getenv("google_maps_key")
    db_engine = sqlalchemy.create_engine(f"sqlite:///{paths.stocking_database}")
    google_client  = googlemaps.Client(key=api_key)

def backup_database() -> None:
    with sqlite3.connect(Utils.paths.value.stocking_database) as conn:
        with open(Utils.paths.value.sql_backup_dir / "backup.sql", "w") as backup_file:
            for line in conn.iterdump():
                backup_file.write(f"{line}\n")
