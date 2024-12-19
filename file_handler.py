import os


class FileHandler:
    _instance = None

    def __new__(cls, filename):
        """A signleton to make only one instance of this class.

        Args:
            filename (str): Database file name. Or just what is the file name to keep/retrieve data.

        Returns:
            FileHandler: An new instance of this class if it's not exist yet. Else just the existing instance.
        """
        if cls._instance is None:
            cls._instance = super(FileHandler, cls).__new__(cls)
            cls._instance.filename = filename
        return cls._instance

    def read_lines(self):
        """Return the lins of the file if it exist. Else just return empty list.

        Returns:
            list of string: lines from the file
        """
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return file.readlines()

    def write_lines(self, lines):
        """Writes lines into the file. Will replace everything.

        Args:
            lines (list of str): list of line to be written.
        """
        with open(self.filename, "w") as file:
            file.writelines(lines)

    # Append lines into the file
    # Make sure to manually add "\n" if you want new line
    def append_lines(self, line):
        """Append lines into the file.It will not add newline. Add yourself.

        Args:
            line (str): The line to be append.
        """
        with open(self.filename, "a") as file:
            file.write(line)
