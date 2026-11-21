import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

boundary = gpd.read_file("data/processed/surulere_boundary_utm31.gpkg")

# Mean NDVI per polygon
with rasterio.open("data/processed/surulere_ndvi.tif") as src:
    polys_ndvi = boundary.to_crs(src.crs)
    ndvi_means = []
    for geom in polys_ndvi.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        ndvi_means.append(float(cells.mean()) if cells.count() > 0 else np.nan)

# Mean elevation per polygon
with rasterio.open("data/raw/lagos_dem.tif") as src:
    polys_dem = boundary.to_crs(src.crs)
    elev_means = []
    for geom in polys_dem.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        elev_means.append(float(cells.mean()) if cells.count() > 0 else np.nan)

boundary["mean_ndvi"] = np.round(ndvi_means, 3)
boundary["mean_elevation_m"] = np.round(elev_means, 1)

out_csv = "month-03/week-12/surulere_zonal_stats.csv"
boundary.drop(columns="geometry").to_csv(out_csv, index=False)
print(boundary[["lganame", "mean_ndvi", "mean_elevation_m"]])
print("Saved", out_csv)