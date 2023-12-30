import json

from Models.stocking_data_model import StockingData
from sqlalchemy.orm import Session
from typing import Generator
from utils import Utils


def search_by_species(species: str) -> Generator[StockingData, None, None]:
    with Session(Utils.db_engine.value) as session:
        db_results = session.query(StockingData).filter(StockingData.species.like(f"%{species}%")).all()
    for result in db_results:
        yield result

def filter_geo_data_response(json_data: any) -> None:
    breakpoint()

def get_geo_data(species: str) -> None:
    for result in search_by_species(species):
        formatted_location = f"{result.stocked_water_body_name}, Wisconsin"
        filter_geo_data_response(json.dump(Utils.google_client.value.geocode(formatted_location)))

get_geo_data("musk")