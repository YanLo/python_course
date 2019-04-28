import tempfile
import os

class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def write(self, line_to_write):
        with open(self.path_to_file, 'w') as f:
            f.write(line_to_write)

    def read(self):
        with open(self.path_to_file, 'r') as f:
            return f.read()

    def __add__(self, other):
        temp_file_path = os.path.join(tempfile.gettempdir(), 'concatenated_file')
        new_file_obj = type(self)(temp_file_path)
        new_file_obj.write(self.read() + other.read())

        return new_file_obj

    def __iter__(self):
        iter_file = open(self.path_to_file, 'r')
        return iter_file

    def __str__(self):
        return self.path_to_file

if __name__ == '__main__':
    file_obj_1 = File('/tmp/first')
    file_obj_1.write('Hi, I am first\n')

    file_obj_2 = File('/tmp/second')
    file_obj_2.write('Hi, I am second\n')

    sum_obj = file_obj_1 + file_obj_2
    for line in sum_obj:
        print(line)
