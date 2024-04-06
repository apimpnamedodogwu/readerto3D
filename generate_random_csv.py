import csv
import random

def generate_random_csv(file_name, num_rows, num_columns):
  """
  Generates a random CSV file and returns the file path.

  Args:
      filename (str): The desired filename for the CSV file.
      num_rows (int): The number of rows to generate in the CSV file.
      num_columns (int): The number of columns to generate in the CSV file.

  Returns:
      str: The filepath of the generated CSV file.
  """
  with open(file_name, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for _ in range(num_rows):
      row = [random.randint(1, 100) for _ in range(num_columns)]
      writer.writerow(row)

  return file_name  

