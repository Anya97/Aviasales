import csv
from database_service import Flights, save_list


def read_data_from_file():
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        flights_list = []
        for row in list(reader)[1:]:
            flights_list.append(Flights(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        save_list(flights_list)