import os


class FileHandler:
    _instance = None

    # Singleton
    def __new__(cls, filename):
        if cls._instance is None:
            cls._instance = super(FileHandler, cls).__new__(cls)
            cls._instance.filename = filename
        return cls._instance

    # Return the lines of the file if it exist
    # Else just return empty list
    def read_lines(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return file.readlines()

    # Writes lines into the file
    # "w" will truncate the file so it will rewrite the file
    def write_lines(self, lines):
        with open(self.filename, "w") as file:
            file.writelines(lines)

    # Append lines into the file
    # Make sure to manually add "\n" if you want new line
    def append_lines(self, line):
        with open(self.filename, "a") as file:
            file.write(line)
