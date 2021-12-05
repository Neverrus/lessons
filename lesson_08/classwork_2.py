
from library import car_list

if __name__ == "__main__":

    year = int(input("Year: "))
    print(filter_cars(car_list, year))

    print(list(y for y in car_list if y["year"] < year))
    print(list(filter(lambda x: x["year"] < year, car_list)))
