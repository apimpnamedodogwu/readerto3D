import rhinoscriptsyntax as rs
from csvreader import CSVReader
from jsonreader import JSONReader  
import generate_random_csv as gen_csv
import generate_random_json_file as gen_json_file


def run():
    # Ask the user whether to read an existing CSV file, JSON file, or generate a random CSV/JSON file
    choice = rs.GetString("Do you want to (1) read an existing CSV file, (2) read an existing JSON file, or (3) generate a random file? (Type '1', '2', or '3')", "1")

    if choice == "1":
        # Read an existing CSV file
        filepath = rs.OpenFileName("Select CSV file to read", "CSV files (*.csv)|*.csv||")
        if not filepath: return
        reader = CSVReader()
        data = reader.ReadData(filepath)
        print("CSV file read successfully!")

    elif choice == "2":
        # Read an existing JSON file
        filepath = rs.OpenFileName("Select JSON file to read", "JSON files (*.json)|*.json||")
        if not filepath: return
        reader = JSONReader()
        data = reader.ReadData(filepath)
        print("JSON file read successfully!")

    elif choice == "3":
        # Generate a random file
        file_type = rs.GetString("Do you want to generate a random (1) CSV file or (2) JSON file? (Type '1' or '2')", "1")
        if file_type == "1":
            # Generate a random CSV file
            num_rows = int(rs.GetInteger("Enter the number of rows for the random CSV file", 10))
            num_columns = int(rs.GetInteger("Enter the number of columns for the random CSV file", 5))
            file = gen_csv.generate_random_csv("random_data.csv", num_rows, num_columns)
            reader = CSVReader()
            reader.ReadData(file)
            print("Random CSV file generated: random_data.csv")

        elif file_type == "2":
            # Generate a random JSON file
            num_objects = int(rs.GetInteger("Enter the number of objects for the random JSON file", 10))
            file = gen_json_file.generate_random_json("random_data.json", num_objects)
            reader = JSONReader()
            data = reader.ReadData(file)
            print("Random JSON file generated:", file)

        else:
            print("Invalid choice for file type. Please type '1' for CSV or '2' for JSON.")

    else:
        print("Invalid choice. Please type '1', '2', or '3'.")

run()
