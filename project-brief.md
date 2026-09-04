# Project Brief: Waste Collection Coverage in Surulere LGA

## 1. The Question
Which residential neighborhoods in Surulere Local Government Area sit more than 1 km from a designated waste collection point or transfer station?

## 2. Why It Matters
Rapid urban density and informal waste disposal in Surulere lead to clogged drainage channels and localized flooding during heavy rains. Knowing which communities lack convenient access to formal waste collection points helps urban planners, LAWMA, and local authorities position new collection bins, transfer loading stations, or PSP (Private Sector Participation) waste routing schedules where they are needed most.

## 3. The Data I Need
- **Administrative Boundary:** Surulere LGA boundary.
- **Waste Facilities & Points:** Designated waste disposal sites, dumpsters, recycling hubs, and transfer stations (e.g., LAWMA Iponri Transfer Loading Station).
- **Road Network:** Primary, secondary, and residential street network for access routing.
- **Settlement/Built-up Extents:** Residential and commercial building fabric or settlement extents to measure uncovered populated zones.

## 4. Where Each Dataset Comes From
- **Surulere LGA Boundary:** GRID3 Nigeria Operational LGA Boundaries — [https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries) — Format: GeoPackage / Shapefile (~15 MB).
- **Waste Collection Points:** OpenStreetMap via QuickOSM (Tags: `amenity=waste_disposal`, `amenity=waste_transfer_station`, `amenity=recycling`) — [https://www.openstreetmap.org](https://www.openstreetmap.org) — Format: GeoPackage (Extracted for Surulere).
- **Road Network:** OpenStreetMap via QuickOSM (Tag: `highway=*`) — [https://www.openstreetmap.org](https://www.openstreetmap.org) — Format: GeoPackage (Extracted for Surulere).
- **Settlement Extents:** GRID3 Nigeria Settlement Extents v4.1 — [https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1) — Format: GeoPackage (~40 MB).

## 5. What I Will Build
A spatial pipeline that buffers existing waste facilities, measures catchment coverage against populated residential areas, and flags service deserts. Over the course of the cohort, this will evolve into an automated API and web map dashboard highlighting areas in need of prioritized waste collection infrastructure.
