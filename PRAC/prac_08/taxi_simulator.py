"""
CP1404 Practical
Taxi Simulator
"""
from prac_06.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_cost = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Lets Drive!")
    print(MENU)
    choice = input(">>>")
    while choice != "q":
        if choice == "c":
            print("Taxis Available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose Taxi"))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Index error")
            except ValueError:
                print("Value error")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                trip_total = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                             trip_total))
                total_cost += trip_total
            else:
                print("Invalid Amount")

        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_cost))
        print(MENU)
        choice = input(">>>")

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(i, taxi)


main()
