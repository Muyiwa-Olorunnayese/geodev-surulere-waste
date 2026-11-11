import geopandas as gpd

boundary = gpd.read_file("data/processed/surulere_boundary_utm31.gpkg").to_crs(epsg=32631)
points = gpd.read_file("data/processed/surulere_points_py.gpkg", layer="waste_points").to_crs(epsg=32631)

joined = gpd.sjoin(
    points,
    boundary[["lganame", "geometry"]],
    how="inner",
    predicate="within"
)

counts = joined.groupby("lganame").size().rename("facility_count").reset_index()
summary = boundary.merge(counts, on="lganame", how="left")
summary["facility_count"] = summary["facility_count"].fillna(0).astype(int)

print(summary[["lganame", "facility_count"]])
print("Total counted facilities inside LGA:", summary["facility_count"].sum(), "of", len(points))