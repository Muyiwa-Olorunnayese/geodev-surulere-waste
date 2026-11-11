import geopandas as gpd
import matplotlib.pyplot as plt

boundary = gpd.read_file("data/processed/surulere_boundary_utm31.gpkg").to_crs(epsg=32631)
points = gpd.read_file("data/processed/surulere_points_py.gpkg", layer="waste_points").to_crs(epsg=32631)

# 1,000-metre buffer around formal waste facilities
reach = points[["geometry"]].copy()
reach["geometry"] = reach.buffer(1000)
reach_dissolved = reach.dissolve()

# Spatial difference to calculate unserviced gap
unserviced = gpd.overlay(boundary, reach_dissolved, how="difference")

# Area calculations
total_area = boundary.geometry.area.sum() / 1_000_000
unserviced_area = unserviced.geometry.area.sum() / 1_000_000
served_area = total_area - unserviced_area
served_pct = (served_area / total_area) * 100
unserviced_pct = (unserviced_area / total_area) * 100

print(f"Total Area: {total_area:.2f} km2")
print(f"Served Area (1 km): {served_area:.2f} km2 ({served_pct:.1f}%)")
print(f"Unserviced Area: {unserviced_area:.2f} km2 ({unserviced_pct:.1f}%)")

# Save processed GeoPackage deliverable
unserviced.to_file("data/processed/surulere_unserviced_py.gpkg", layer="unserviced_zones")
print("Saved data/processed/surulere_unserviced_py.gpkg")

# Plot and save map PNG
fig, ax = plt.subplots(figsize=(8, 8))
boundary.plot(ax=ax, color="#FAFAFA", edgecolor="#212121", linewidth=1.2)
unserviced.plot(ax=ax, color="#FFE0B2", edgecolor="#FB8C00", hatch="//", alpha=0.7, label=f"Unserviced ({unserviced_pct:.1f}%)")
points.plot(ax=ax, color="#D32F2F", markersize=40, zorder=4, label="Waste Points")

ax.set_title(f"Surulere Waste Service Gap (1 km Reach): {unserviced_pct:.1f}% Unserviced", fontsize=11)
ax.set_axis_off()
fig.savefig("month-03/week-11/my_reach_map.png", dpi=150, bbox_inches="tight")
print("Saved month-03/week-11/my_reach_map.png")