# Week 11: Coordinate reference systems and spatial operations in code

## What this folder contains
- `area_wrong_and_right.py`: Demonstrates area calculation distortion in geographic degrees versus projected metric units.
- `set_vs_to.py`: Illustrates the distinction between relabelling metadata with `set_crs` and recalculating coordinates with `to_crs`.
- `one_point.py`: Transforms single point coordinates from degrees to UTM easting and northing using `pyproj`.
- `spatial_ops.py`: Implements point buffering, spatial join (`within`), and counting facilities per polygon.
- `coverage_gap.py`: Computes spatial deficit percentages using dissolved buffers and overlay difference.
- `nearest.py`: Measures metric distance from polygon centroids to the nearest facility using `sjoin_nearest`.
- `clip_dissolve.py`: Clips linear features to polygon boundaries and dissolves administrative units into an overall outline.
- `fix_geometry.py`: Identifies invalid self-intersecting polygon geometries and repairs them with `make_valid`.
- `my_crs.py`: Reprojects the Surulere boundary layer to EPSG:32631 and calculates metric land area.
- `my_count.py`: Performs an inner spatial join to count municipal waste transfer points inside the LGA boundary.
- `my_reach.py`: Runs a 1,000-metre buffer and geometric difference to measure the unserviced waste gap in Surulere LGA.
- `my_validity.py`: Evaluates geometry validity on the study area polygon layer.
- `my_reach_map.png`: Analytical map rendering the 1 km facility reach against unserviced residential zones.

## How to run it
From the repository root:
```bash
uv run month-03/week-11/area_wrong_and_right.py
uv run month-03/week-11/spatial_ops.py
uv run month-03/week-11/my_crs.py
uv run month-03/week-11/my_count.py
uv run month-03/week-11/my_reach.py
uv run month-03/week-11/my_validity.py