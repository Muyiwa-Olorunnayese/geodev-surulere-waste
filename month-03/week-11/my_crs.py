import geopandas as gpd

boundary = gpd.read_file("data/processed/surulere_boundary_utm31.gpkg")
print("Original CRS:", boundary.crs)
print("Estimated UTM:", boundary.estimate_utm_crs())

# Ensure projection to EPSG:32631 (WGS 84 / UTM Zone 31N)
boundary_utm = boundary.to_crs(epsg=32631)
area_m2 = boundary_utm.geometry.area.sum()
area_km2 = area_m2 / 1_000_000

print(f"Surulere LGA Total Area: {round(area_km2, 2)} km2")