import csv
import sqlite3
from math import radians, sin, cos, sqrt, atan2


# Connect to (or create) a SQLite database
connection = sqlite3.connect('C:\\Users\\rakes\\hackathon\\pincodes.db')
cursor = connection.cursor()
print("a")
# Create a table (if it doesn't exist already)
cursor.execute('''CREATE TABLE IF NOT EXISTS pincode
                 (area varchar(255) primary key, pincode bigint, latitude float, longitude float)''')
print("b")
# Open the CSV file
with open("C:\\Users\\rakes\\hackathon\\BangaloreAreaLatLongDetails.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)  # Skip the header row
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        # Insert each row into the database
        cursor.execute('''INSERT OR IGNORE INTO pincode (area,pincode, latitude,longitude) VALUES (?, ?, ?, ?)''', row)
        print(row)
print("c")
# Commit the transaction
connection.commit()

# Close the connection
connection.close()


# Haversine function to calculate distance in kilometers between two coordinates
def haversine(coord1, coord2):
    # Radius of the Earth in km
    R = 6371.0

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = radians(lat1), radians(lon1)
    lat2, lon2 = radians(lat2), radians(lon2)

    # Difference in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c  # Output distance in kilometers

    return distance

