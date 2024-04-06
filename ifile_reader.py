class IFileReader:
    """
    This interface defines methods for reading data from files.
    """

    def ReadData(self, file_path):
        """
        This method reads data from a file and returns it as a list.

        Args:
          filepath: Path to the file to be read.

        Returns:
          A list containing the parsed data.
        """
        pass

class IFileWriter:
    """
    This interface defines methods for writing data to files.
    (Optional in this case)
    """

    def WriteData(self, file_path, data):
        """
        This method writes data to a file.

        Args:
          filepath: Path to the file to be written.
          data: The data to be written (list or dictionary).
        """
        pass
