from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import declarative_base

base = declarative_base()

class StockingData(base):
    __tablename__ = "WIDNR_Stocking_Data"
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    source = Column(String)
    stocked_water_body_name = Column(String)
    local_waterbody_name = Column(String)
    species = Column(String)
    strain = Column(String)
    age_class = Column(String)
    nbr_stocked = Column(Integer)
    avg_len_inches = Column(Float)

    def __repr__(self) -> str:
        return f"""
ID: {self.id}
Year: {self.year}
Source: {self.source}
Stocked Water Body Name: {self.stocked_water_body_name}
Local Water Body Name: {self.local_waterbody_name}
Species: {self.species}
Strain: {self.strain}
Age Class: {self.age_class}
Stocked #: {self.nbr_stocked}
Avg. Length(in): {self.avg_len_inches}
"""