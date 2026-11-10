import geopandas as gpd

layer_path = "data/processed/surulere_boundary_utm31.gpkg"
print("Layers in file:", gpd.list_layers(layer_path))

boundary = gpd.read_file(layer_path)
print("Preview:\n", boundary.head())
print("Rows and columns:", boundary.shape)
print("Geometry types:\n", boundary.geom_type.value_counts())
print("CRS:", boundary.crs)
print("Bounds (minx, miny, maxx, maxy):", boundary.total_bounds)