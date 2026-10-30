import csv

def read_data(filename):
    """Reads a CSV file and returns a list of row dictionaries."""
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_value(raw):
    """Cleans a string value and converts it to a float, or returns None if invalid."""
    if raw is None:
        return None
    val = raw.strip()
    if val == "" or val in ["NA", "N/A", "-", "null"]:
        return None
    try:
        return float(val.replace(",", ""))
    except ValueError:
        return None

def summarise_column(rows, column):
    """Extracts numeric values for a column and returns count, min, max, and mean."""
    values = []
    for row in rows:
        val = clean_value(row.get(column))
        if val is not None:
            values.append(val)
    
    if not values:
        return None
    
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": round(sum(values) / len(values), 4)
    }

def summarise_all(filename, columns):
    """Coordinates reading, summarizing, and printing one line per column."""
    rows = read_data(filename)
    for col in columns:
        stats = summarise_column(rows, col)
        if stats:
            print(f"{col}: count={stats['count']}, smallest={stats['smallest']}, largest={stats['largest']}, average={stats['average']}")
        else:
            print(f"{col}: no numeric data found")

# Run on the two numeric coordinates from your Month 1 waste points dataset
if __name__ == "__main__":
    summarise_all("surulere_waste_points.csv", ["longitude", "latitude"])