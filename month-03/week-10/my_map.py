import geopandas as gpd
import matplotlib.pyplot as plt

boundary = gpd.read_file("data/processed/surulere_boundary_utm31.gpkg")
points = gpd.read_file("data/processed/surulere_points_py.gpkg", layer="waste_points")

# Reproject points to match boundary projected CRS
points_proj = points.to_crs(boundary.crs)

fig, ax = plt.subplots(figsize=(8, 8))
boundary.plot(ax=ax, color="#FFF3E0", edgecolor="#E65100", linewidth=1.5)
points_proj.plot(ax=ax, color="#B71C1C", markersize=45, zorder=3)

for x, y, label in zip(points_proj.geometry.x, points_proj.geometry.y, points_proj["name"]):
    ax.annotate(label, xy=(x, y), xytext=(5, 5), textcoords="offset points", fontsize=8)

ax.set_title("Municipal Waste Infrastructure - Surulere LGA")
ax.set_axis_off()
fig.savefig("month-03/week-10/my_map.png", dpi=150, bbox_inches="tight")
print("Saved month-03/week-10/my_map.png")