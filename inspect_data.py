import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "" or raw in ["NA", "N/A", "-"]:
            continue
        values.append(float(raw.replace(",", "")))
        
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }

lon_summary = inspect_column("surulere_waste_points.csv", "longitude")
lat_summary = inspect_column("surulere_waste_points.csv", "latitude")

print("Longitude:", lon_summary)
print("Latitude:", lat_summary)
