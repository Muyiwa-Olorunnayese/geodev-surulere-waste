# Month 1 Summary: Solid Waste Management Accessibility in Surulere LGA

## 1. Research Question
Which residential communities in Surulere Local Government Area fall outside a 1-kilometer catchment of formal municipal solid waste disposal facilities and transfer loading stations?

---

## 2. Spatial Operation Executed and Rationale
- **Operation:** 1,000-meter (1 km) Euclidean Buffer (Dissolved), followed by a Geometric Clip to the study area boundary.
- **Why this operation:** In urban solid waste management, 1 kilometer represents an accessible transit threshold for primary waste collection and localized cart/truck turnaround to an intermediate transfer point. Running this operation in a metric projected coordinate system (EPSG:32631 — WGS 84 / UTM Zone 31N) defines the exact spatial envelope serviced by formal municipal waste infrastructure.

---

## 3. Expectations vs. Results

### Prior Expectations
- **Feature Count:** Expected 1 dissolved multi-part polygon layer covering the service catchments.
- **Coverage Values:** Expected moderate coverage (~40–50%) across the LGA, anticipating that transfer stations would be centrally positioned to serve high-density neighborhoods.

### Actual Results & Four-Way Verification
1. **Visual Inspection:** Buffers cleanly clustered along the southern and eastern edges of Surulere, leaving the entire northern and central core blank.
2. **Row Count Verification:** The dissolved buffer produced exactly **1 multi-polygon feature**, matching expectations.
3. **Manual Measurement Verification:** Measured the radius from the LAWMA Iponri TLS point to the outer buffer curve using the QGIS Measure Tool; confirmed exactly 1,000 meters.
4. **Empty Geometry Check:** Ran geometry validation; zero null geometries or self-intersections detected.
5. **Spatial Extent:** Formal service coverage spans less than **30%** of Surulere's land area, leaving over **70%** of the LGA in the unserved zone.

---

## 4. Key Surprises
- **Peripheral Clustering:** Formal infrastructure is strictly peripheral (Iponri, Costain corridor, Orile border), rather than distributed near high-generation residential hubs.
- **Complete Central Void:** High-density, high-traffic neighborhoods—such as Lawanson, Itire, Aguda, and Adelabu—have zero formal transfer facilities within a 1 km radius, explaining heavy reliance on informal PSP cart operations and vulnerable roadside accumulation points.

---

## 5. Outstanding Data Needs
- **Informal & Communal Bin Coordinates:** Geolocation data for neighborhood communal collection bins and PSP compactor staging points to map localized micro-catchments.
- **Road Network Impedance:** Speed limit and congestion data across major corridors (e.g., Western Avenue, Ojuelegba) to run network-time service areas rather than straight-line Euclidean buffers.
- **High-Resolution Population Rasters:** GRID3 or WorldPop settlement rasters to quantify the exact number of residents living within the unserviced zones.
