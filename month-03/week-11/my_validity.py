import geopandas as gpd

boundary = gpd.read_file("data/processed/surulere_boundary_utm31.gpkg")

invalid_count = (~boundary.is_valid).sum()
print("Invalid geometries before repair:", invalid_count)

if invalid_count > 0:
    boundary["geometry"] = boundary.make_valid()
    print("Invalid geometries after repair:", (~boundary.is_valid).sum())
else:
    print("All boundary geometries are structurally valid.")