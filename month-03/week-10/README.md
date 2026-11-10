# Week 10: GeoPandas, Layers as tables

## What this folder contains
- `explore_pandas.py`: Reads and summarises ward population tabular data.
- `filter_sort.py`: Filters rows by threshold, sorts records, and creates calculated columns.
- `explore_layer.py`: Inspects layer metadata, geometry types, CRS, and coordinate bounds.
- `geom_props.py`: Evaluates Shapely geometries for validity and centroid coordinates.
- `csv_to_points.py`: Converts coordinate columns into a GeoDataFrame and exports to GeoPackage.
- `join_population.py`: Attribute merge testing match counts before and after text cleaning.
- `make_map.py`: Plots ward polygons with facility overlays.
- `save_outputs.py`: Writes layers to GeoPackage and exports tabular attributes to CSV.
- `facilities_map.png`: Generated map of health facilities across Ibadan North wards.
- `wards_table.csv`: Exported tabular attribute data.
- `my_explore.py`: 5-point inspection checklist on Surulere LGA boundary.
- `my_points.py`: Builds a GeoPackage point layer from Surulere waste facility coordinates.
- `my_join.py`: Attribute join validating standardized administrative keys.
- `my_map.py`: Generates the Surulere waste facilities map.
- `my_map.png`: Map of Surulere LGA boundary and facility points.

## How to run it
From the repository root:
```bash
uv run month-03/week-10/explore_pandas.py
uv run month-03/week-10/csv_to_points.py
uv run month-03/week-10/join_population.py
uv run month-03/week-10/make_map.py
uv run month-03/week-10/my_explore.py
uv run month-03/week-10/my_points.py
uv run month-03/week-10/my_join.py
uv run month-03/week-10/my_map.py