import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
facilities = gpd.read_file("data/processed/facilities.gpkg", layer="facilities")

fig, ax = plt.subplots(figsize=(7, 8))
wards.plot(ax=ax, color="#E0F2F1", edgecolor="#004D40")
facilities.plot(ax=ax, color="#D84315", markersize=10)
ax.set_title("Health facilities in Ibadan North")
ax.set_axis_off()
fig.savefig("month-03/week-10/facilities_map.png", dpi=150, bbox_inches="tight")
print("Map saved")