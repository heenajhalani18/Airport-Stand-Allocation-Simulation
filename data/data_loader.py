import csv

def load_aircraft_data(csv_path):
    aircraft_data = []

    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            aircraft_data.append({
                "aircraft_id": row["aircraft_id"],
                "arrival_time": int(row["arrival_time"]),
                "departure_time": int(row["departure_time"])
            })

    return aircraft_data
