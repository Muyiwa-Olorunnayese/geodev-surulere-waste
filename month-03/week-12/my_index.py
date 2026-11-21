import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from rasterio.mask import mask

# Update with your downloaded Lagos Landsat scene prefix
folder = "data/raw/landsat/"
scene = "LC08_L2SP_191055_20260221_20260227_02_T1"

with rasterio.open(folder + scene + "_SR_B4.TIF") as src:
    profile = src.profile
    red_raw = src.read(1).astype("float32")
    raster_crs = src.crs

with rasterio.open(folder + scene + "_SR_B5.TIF") as src:
    nir_raw = src.read(1).astype("float32")

valid = (red_raw > 0) & (nir_raw > 0)
red = red_raw * 0.0000275 - 0.2
nir = nir_raw * 0.0000275 - 0.2

ndvi = np.full(red.shape, -9999, dtype="float32")
total = nir + red
ok = valid & (total != 0)
ndvi[ok] = (nir[ok] - red[ok]) / total[ok]

print("NDVI range:", round(float(ndvi[ok].min()), 3), "to", round(float(ndvi[ok].max()), 3))
print("Mean NDVI:", round(float(ndvi[ok].mean()), 3))

profile.update(dtype="float32", nodata=-9999, count=1)
out_tif = "data/processed/surulere_ndvi.tif"
with rasterio.open(out_tif, "w", **profile) as dst:
    dst.write(ndvi, 1)

# Clip NDVI to Surulere boundary for a clean study-area map
boundary = gpd.read_file("data/processed/surulere_boundary_utm31.gpkg").to_crs(raster_crs)
with rasterio.open(out_tif) as src:
    clipped_ndvi, _ = mask(src, boundary.geometry, crop=True, filled=False)

fig, ax = plt.subplots(figsize=(7, 8))
img = ax.imshow(clipped_ndvi[0], cmap="RdYlGn", vmin=-0.2, vmax=0.9)
fig.colorbar(img, ax=ax, label="NDVI")
ax.set_title("Vegetation Index (NDVI) - Surulere LGA")
ax.set_axis_off()
fig.savefig("month-03/week-12/my_map.png", dpi=150, bbox_inches="tight")
print("Saved month-03/week-12/my_map.png")