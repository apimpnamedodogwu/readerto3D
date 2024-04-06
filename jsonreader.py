import json
import rhinoscriptsyntax as rs
from ifile_reader import IFileReader

class JSONReader(IFileReader):
    def ReadData(self, file_path):
        """
        Reads data from a JSON file and returns a list of points.

        Args:
          filepath: Path to the JSON file.

        Returns:
          A list of Point3d objects representing the data points.
        """
        points = []
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for item in data:
                try:
                    x, y, z = float(item['x']), float(item['y']), float(item['z'])
                    points.append(rs.Point3d(x, y, z))
                except ValueError:
                    print(f"Error parsing item: {item}")  

        return points
