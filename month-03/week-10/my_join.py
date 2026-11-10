import geopandas as gpd
import pandas as pd

boundary = gpd.read_file("data/processed/surulere_boundary_utm31.gpkg")

# Attribute table to join with deliberate casing/spacing variations
ops_data = pd.DataFrame({
    "target_lga": ["Surulere", "SURULERE LGA", "surulere "],
    "target_waste_tons_per_day": [450, 450, 450]
})

# First try: raw merge without string cleaning
first_try = boundary.merge(ops_data, left_on="lganame", right_on="target_lga", how="left")
matched_before = first_try["target_waste_tons_per_day"].notna().sum()
print("Matched before cleaning:", matched_before, "of", len(boundary))

def clean_key(text):
    return str(text).strip().upper().replace(" LGA", "")

boundary["join_key"] = boundary["lganame"].apply(clean_key)
ops_data["join_key"] = ops_data["target_lga"].apply(clean_key)

# Second try: merge on standardized join key
joined = boundary.merge(ops_data, on="join_key", how="left")
matched_after = joined["target_waste_tons_per_day"].notna().sum()
print("Matched after cleaning:", matched_after, "of", len(boundary))
print(joined[["lganame", "target_waste_tons_per_day"]])