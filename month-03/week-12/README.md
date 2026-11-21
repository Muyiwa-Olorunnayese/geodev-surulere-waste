# Week 12: Rasters with Rasterio

## What this folder contains
- `inspect_raster.py`: Inspects raster dimensions, bands, data type, CRS, pixel size, bounds and transform.
- `read_values.py`: Reads raster arrays and handles nodata cells safely using masked arrays.
- `pixel_coords.py`: Converts between pixel row/column indices and map coordinates.
- `sample_points.py`: Extracts raster elevation values at point coordinates.
- `ndvi.py`: Applies Landsat Collection 2 Level-2 scale factors and computes NDVI.
- `plot_raster.py`: Renders the NDVI array with a colour bar (`ndvi_map.png`).
- `clip_raster.py`: Clips the DEM to the dissolved study area boundary.
- `zonal_stats.py`: Calculates mean elevation per polygon using masked array clipping.
- `reproject_raster.py`: Warps a raster to a target CRS using bilinear resampling.
- `ndvi_map.png`: Rendered NDVI map for the Ibadan North teaching dataset.
- `my_inspect.py`: Inspects the Lagos DEM and verifies that width times pixel size equals right minus left bounds.
- `my_index.py`: Computes NDVI for Surulere LGA and exports `my_map.png`.
- `my_zonal.py`: Summarises mean NDVI and mean elevation for Surulere LGA into `surulere_zonal_stats.csv`.
- `surulere_zonal_stats.csv`: Zonal statistics summary table for Surulere LGA.
- `my_map.png`: Clipped NDVI map of Surulere LGA.

## How to run it
From the repository root:
```bash
uv run month-03/week-12/inspect_raster.py
uv run month-03/week-12/ndvi.py
uv run month-03/week-12/plot_raster.py
uv run month-03/week-12/my_inspect.py
uv run month-03/week-12/my_index.py
uv run month-03/week-12/my_zonal.py