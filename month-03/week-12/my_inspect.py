import rasterio

dem_path = "data/raw/lagos_dem.tif"

with rasterio.open(dem_path) as src:
    print("Width x height:", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data type:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src.bounds)
    print("Nodata:", src.nodata)
    print("Transform:\n", src.transform)

    calc_width = round(src.width * src.res[0], 6)
    bounds_width = round(src.bounds.right - src.bounds.left, 6)
    print(f"Width check: {calc_width} vs {bounds_width} (Match: {calc_width == bounds_width})")