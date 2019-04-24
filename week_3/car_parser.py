import csv
import os

class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)

class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(self, car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(self, car_type, brand, photo_file_name, carrying)
        self.body_whl = body_whl
        val_list = self.body_whl.split("x")
        if (val_list == ['']):
            self.body_length = self.body_width = self.body_hight = 0
        else:
            try:
                self.body_length = float(body_parameters_list[0])
                self.body_width = float(body_parameters_list[1])
                self.body_hight = float(body_parameters_list[2])
            except ValueError:
                self.body_length = self.body_width = self.body_hight = 0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_hight

class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(self, car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)
        for row in reader:
            print(row)

    return car_list

if __name__ == "__main__":
    print(get_car_list("cars.csv"))
