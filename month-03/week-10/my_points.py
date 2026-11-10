import pandas as pd
import geopandas as gpd

df = pd.read_csv("surulere_waste_points.csv")
print("Raw point rows:", len(df))

points = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["longitude"], df["latitude"]),
    crs="EPSG:4326"
)
print("CRS:", points.crs)
print(points[["name", "facility_t", "geometry"]])

points.to_file("data/processed/surulere_points_py.gpkg", layer="waste_points")
print("Saved data/processed/surulere_points_py.gpkg")