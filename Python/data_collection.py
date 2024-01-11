from Models.stocking_data_model import StockingData
from sqlalchemy.orm import Session
from typing import Generator
from utils import Utils, backup_database


def search_by_species(species: str) -> Generator[StockingData, None, None]:
    with Session(Utils.db_engine.value) as session:
        db_results = session.query(StockingData).filter(StockingData.species.like(f"%{species}%")).all()
    for result in db_results:
        yield result

def filter_geo_data_response(json_data: any, data_model: StockingData) -> None:
    data_model.latitude = json_data[0]["geometry"]["location"]["lat"]
    data_model.longitude = json_data[0]["geometry"]["location"]["lng"]
    with Session(Utils.db_engine.value) as session:
        session.query(StockingData).filter(StockingData.id == data_model.id).update({"latitude": data_model.latitude, "longitude": data_model.longitude})
        session.commit()    

def get_geo_data(species: str) -> None:
    for result in search_by_species(species):
        if result.latitude is None or result.longitude is None:
            formatted_location = f"{result.stocked_water_body_name}, Wisconsin"
            filter_geo_data_response(Utils.google_client.value.geocode(formatted_location), result)

print("Starting..")
get_geo_data("muskellunge")
backup_database()
print("Done!")