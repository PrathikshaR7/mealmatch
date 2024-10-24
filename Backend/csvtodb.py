import csv
import sqlite3

# Connect to (or create) a SQLite database
connection = sqlite3.connect('C:\\Users\\rakes\\hackathon\\new\\ngofood.db')
cursor = connection.cursor()
print("a")
# Create a table (if it doesn't exist already)
cursor.execute('''CREATE TABLE IF NOT EXISTS ngo_details
                 (name varchar(255) primary key, del varchar(65535), address varchar(65535))''')
print("b")
# Open the CSV file
with open("C:\\Users\\rakes\\hackathon\\new\\csv-files.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)  # Skip the header row
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        # Insert each row into the database
        cursor.execute('''INSERT OR IGNORE INTO ngo_details (name, "del", address) VALUES (?, ?, ?)''', row)
        print(row)
print("c")
# Commit the transaction
connection.commit()

# Close the connection
connection.close()
