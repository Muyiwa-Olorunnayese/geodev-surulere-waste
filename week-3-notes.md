# Week 3 Data Processing & Quality Assurance: Waste Logistics in Surulere LGA

## 1. Coordinate Reference System (CRS) Selection
- **Chosen CRS:** EPSG:32631 — WGS 84 / UTM Zone 31N
- **Justification:** The raw OpenStreetMap and GRID3 data were provided in EPSG:4326 (WGS 84 geographic coordinates in degrees). To measure physical distances (e.g., 1 km catchment buffers) and surface areas in metric units rather than decimal degrees, data must be in a conformal projected coordinate system. Surulere LGA, Lagos, falls within UTM Zone 31N, making EPSG:32631 the standard projection for accurate spatial measurements.

---

## 2. Reprojection and Clipping Summary
- **Reprojected Layers (to EPSG:32631):**
  - Surulere LGA Boundary (`data/processed/surulere_boundary_utm31.gpkg`)
  - Waste Management Facilities & Hubs (`data/processed/waste_facilities_utm31.gpkg`)
  - OpenStreetMap Road Network (`data/processed/surulere_roads_utm31.gpkg`)
- **Clipped Layers:**
  - OpenStreetMap Road Network clipped to `surulere_boundary_utm31` to eliminate surrounding road features across neighboring LGAs.
  - 1 km Facility Buffer dissolved catchment clipped to the Surulere boundary.

---

## 3. Results of the Five Quality Checks

### Check 1: CRS Consistency Check
- **Expectation:** All operational layers share identical projection parameters (`EPSG:32631`).
- **Result:** **Pass**. All layers verified in QGIS Layer Properties under Information/Source. Distance tools measure natively in meters.

### Check 2: Spatial Extent & Alignment Check
- **Expectation:** Features visually align without spatial shift or offset against base imagery.
- **Result:** **Pass**. Verified against Google Satellite and OpenStreetMap standard tiles. Road centerlines align with the boundary without georeferencing displacement.

### Check 3: Geometry Validity Check
- **Expectation:** No self-intersecting polygons, duplicate nodes, or null geometries.
- **Result:** **Pass**. Ran QGIS *Check Validity* on the Surulere boundary polygon and waste facility points. No invalid geometries detected.

### Check 4: Completeness & Attribute Audit
- **Expectation:** Necessary attribute fields exist with minimal critical NULL values.
- **Result:** **Flagged & Documented**. 
  - OpenStreetMap queries for `amenity=waste_disposal` and `amenity=waste_transfer_station` yielded 0 features across Surulere LGA.
  - Mitigated by digitizing verified municipal infrastructure (LAWMA Iponri TLS, Orile Landfill interface, Costain Depot, LAWMA Mainland Yard). 
  - Road attribute `surface` contains nulls, which is flagged for future network impedance modeling.

### Check 5: Bounding Box & Clip Verification
- **Expectation:** No stray features exist outside the Surulere administrative envelope.
- **Result:** **Pass**. Road networks and localized facility service zones terminate neatly at the study area perimeter.

---

## 4. Problems Identified, Resolutions, and Flags
- **Problem 1 (OGR SQLite Error):** Relative/root file paths initially failed to create GeoPackage databases.
  - *Fix:* Configured explicit folder destinations (`data/processed/`) within the local repository directory.
- **Problem 2 (CRS Degree Units in Buffer Tool):** Early buffer operations defaulted to degrees rather than meters.
  - *Fix:* Explicitly reprojected input layers to EPSG:32631 via *Vector → Data Management Tools → Reproject Layer* before buffer execution.
- **Problem 3 (OSM Point Data Deficit):** OpenStreetMap lacks communal municipal bin locations.
  - *Status:* Flagged in data notes; resolved for macro-level analysis by digitizing formal LAWMA transfer hubs.

---

## 5. Location of Analysis-Ready Files
All cleaned, projected, and clipped layers are stored in the repository under:
- `data/processed/surulere_boundary_utm31.gpkg`
- `data/processed/waste_facilities_utm31.gpkg`
- `data/processed/surulerearea_waste.gpkg` (clipped road network)
- `data/processed/waste_catchment_1km_clipped.gpkg`
- `data/processed/new_unserviced_waste_zones.gpkg`
