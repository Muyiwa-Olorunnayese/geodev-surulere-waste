# Data Notes: Solid Waste Logistics and Catchment in Surulere LGA

## 1. GRID3 Nigeria Operational LGA Boundaries
- **Source & Link:** [GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries)
- **Version & Date:** Operational LGA Boundaries (v2.0 / v3.0)
- **Downloaded On: 12th September 2026
- **Format:** GeoPackage (.gpkg)
- **Feature Count:** 774 national features (filtered to 1 feature: Surulere LGA)
- **Geometry Type:** Polygon / MultiPolygon
- **Key Columns:** `lga_name` (Surulere), `state_name` (Lagos), `lga_code` (25018)
- **CRS:** EPSG:4326 (WGS 84 geographic)
- **Quality & Gaps:** Complete national coverage with no null values in administrative name columns. Aligns with official Lagos State administrative demarcations and serves as the master study boundary.

---

## 2. OpenStreetMap Landfill Polygon (via QuickOSM)
- **Source & Link:** [OpenStreetMap](https://www.openstreetmap.org) via QuickOSM plugin
- **Extraction Query:** `landuse=landfill` within Surulere extent
- **Extracted On: 12th September 2026
- **Format:** GeoPackage (`data/raw/osm_landfill_polygons.gpkg`)
- **Feature Count:** 1 feature (OSM ID: `786992206`)
- **Geometry Type:** MultiPolygon
- **CRS:** EPSG:4326 (WGS 84 geographic)
- **Quality & Gaps:**
  - **Completeness:** Severe mapping deficit. Queries for `amenity=waste_disposal`, `amenity=waste_transfer_station`, and `amenity=recycling` returned 0 features across the LGA. Only a single dumpsite/landfill parcel near Orile-Iganmu was present in OSM.
  - **Positional Accuracy:** Coincides with the rail corridor / expressway margin near the southern edge of Surulere (~6.478°N, 3.348°E).

---

## 3. Digitized Waste Transfer & Logistics Hubs
- **Source & Link:** Primary digitization of verified municipal facilities (LAWMA operational network)
- **Created On: 12th September 2026
- **Format:** GeoPackage (`data/raw/surulere_waste_points.gpkg`)
- **Feature Count:** 4 features
- **Geometry Type:** Point
- **CRS:** EPSG:4326 (WGS 84 geographic)
- **Features Digitized:**
  1. *LAWMA Iponri TLS* (`3.3662, 6.4915`, `transfer_station`)
  2. *Orile Landfill Site* (`3.3491, 6.4784`, `landfill`)
  3. *Costain Waste Depot* (`3.3718, 6.4795`, `depot`)
  4. *LAWMA Mainland Yard* (`3.3792, 6.4710`, `logistics_hub`)
- **Quality & Gaps:**
  - **Operational Restriction:** These are intermediate mechanical Transfer Loading Stations (TLS) and administrative bases reserved for authorized PSP compactor trucks, not walk-up communal dumpsters.
  - **Analytical Impact:** Buffers around these sites model vehicle turnaround service zones rather than direct pedestrian drop-off catchments.

---

## 4. OpenStreetMap Road Network (via QuickOSM)
- **Source & Link:** [OpenStreetMap](https://www.openstreetmap.org) via QuickOSM plugin
- **Extraction Query:** `highway=*` within Surulere study area extent
- **Extracted On:12th September 2026
- **Format:** GeoPackage (`data/raw/osm_roads.gpkg`)
- **Geometry Type:** LineString / MultiLineString
- **CRS:** EPSG:4326 (WGS 84 geographic)
- **Quality & Gaps:**
  - **Completeness:** High density across central Surulere (Bode Thomas, Western Avenue, Adeniran Ogunsanya, Ogunlana Drive).
  - **Attribute Accuracy:** `surface` attribute is largely null, preventing automated filtering of paved vs. unpaved roads.

---

## Quality Summary & Project Verdict
- **Good Enough For:** Simulating municipal compactor truck accessibility and identifying peripheral residential communities falling outside primary transfer station coverage.
- **Not Good Enough For:** Evaluating household-level pedestrian walkability, as neighborhood communal dustbins are unmapped in open repositories.
