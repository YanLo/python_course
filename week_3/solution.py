class FileReader():
    
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def read(self):
        try:
            with open(self.path_to_file, 'r') as input_file:
                read_string = input_file.read()
                return read_string
        except IOError:
            return ""

if __name__ == "__main__":
    reader = FileReader("example.txt")
    print(reader.read())
