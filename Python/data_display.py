import pandas as pd
import plotly.express as px
import plotly.io as pio

from Models.stocking_data_model import StockingData
from sqlalchemy.orm import Session
from utils import Utils

with Session(Utils.db_engine.value) as session:
    df = pd.read_sql_query(session.query(StockingData).filter(StockingData.species.like("%trout%")).statement, session.bind)
fig = px.scatter_mapbox(df, lat=df["latitude"], lon=df["longitude"], hover_name="species", hover_data=["stocked_water_body_name", "age_class", "year"], color=df["nbr_stocked"], zoom=3, height=1200)
fig.update_layout(mapbox_style="open-street-map")
fig.show(renderer="browser")
