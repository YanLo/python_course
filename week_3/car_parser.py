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
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_length = self.body_width = self.body_height = 0
        val_list = body_whl.split("x")
        if (val_list != ['']):
            self.body_length = float(val_list[0])
            self.body_width = float(val_list[1])
            self.body_height = float(val_list[2])

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type = row[0]
                brand = row[1]
                passenger_seats_count = row[2]
                photo_file_name = row[3]
                body_whl = row[4]
                carrying = row[5]
                extra = row[6]
                if(car_type == 'car'):
                    new_car = Car(car_type, brand, photo_file_name, carrying, passenger_seats_count)
                    car_list.append(new_car)
                if(car_type == 'truck'):
                    new_car = Truck(car_type, brand, photo_file_name, carrying, body_whl)
                    car_list.append(new_car)
                if(car_type == 'spec_machine'):
                    new_car = SpecMachine(car_type, brand, photo_file_name, carrying, extra)
                    car_list.append(new_car)
            except Exception as exception:
                pass
                #print("-----------------EXCEPTION_OCCURED:   ", exception)

    return car_list

#if __name__ == "__main__":
#    car_list = get_car_list("cars.csv")
#    for car in car_list:
#        print(car.car_type, car.brand)

