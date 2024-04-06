import csv
from ifile_reader import IFileReader 
import rhinoscriptsyntax as rs

class CSVReader(IFileReader):
  def ReadData(self, file_path):
    """
    Reads data from a CSV file and returns a list of points.

    Args:
      filepath: Path to the CSV file.

    Returns:
      A list of Point3d objects representing the data points.
    """
    points = []
    with open(file_path, 'r') as csv_file:
      reader = csv.reader(csv_file, delimiter=',')  # Adjust delimiter if needed
      for row in reader:
        try:
          x, y, z = float(row[0]), float(row[1]), float(row[2])  # Assuming 3D data
          points.append(rs.Point3d(x, y, z))
        except ValueError:
          print(f"Error parsing row: {row}")  # Handle potential errors

    return points
