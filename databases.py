#Sarah Scholz, G00364736
#Applied Databases Project 2019
#4.4.1, Python Program

#Main 

#import modules
import sarahsmysql
import sarahsmongodb

def display_menu():
    print()
    print("World DB")
    print("--------")
    print()
    print("MENU")
    print("====")
    print("1 - View 15 Cities")
    print("2 - View Cities by population")
    print("3 - Add New City")
    print("4 - Find Car by Engine Size")
    print("5 - Add New Car")
    print("6 - View Countries by name")
    print("7 - View Countries by population")
    print("x - Exit application")

def main():
    while True:
        display_menu()
        choice = input("Choice:")
        if choice == "x":
            break
        elif choice == "1":
            cities = sarahsmysql.view_15_cities()
            for city in cities:
                print(city["ID"],"|", city["Name"], "|", city["CountryCode"],"|", city["District"],"|", city["Population"])
            
        elif choice == "2":
            print("Cities by Population")
            print("---------------------")
            op = input("Input operator >,< or = :")
            find_population = input("Population: ")
            cities_by_pop = sarahsmysql.cities_by_population(op,find_population)
            for city in cities_by_pop:
                print(city["ID"],"|", city["Name"], "|", city["CountryCode"],"|", city["District"],"|", city["Population"])

        elif choice == "3":
            print("Add new City record")
            print("---------------------")
            city_name = input("Enter city name :")
            country_code = input("Country Code:")
            district = input("District:")
            population = input("Population:")
            sarahsmysql.enter_new_city(city_name,country_code,district,population )
            
        elif choice == "4":
            print("Show cars by engine size")
            print("---------------------")
            engine_size = float(input("Enter an engine size:"))
            cars = sarahsmongodb.find_car(engine_size)
            for car in cars:
                print(car["_id"],"|",car["car"],"|",car["addresses"])

        elif choice == "5":
            print("Add car into database")
            print("---------------------")
            car_id = input("Enter ID: ")
            reg = input("Enter a registration number: ")
            engine_s = input("Enter an engine size: ")
            sarahsmongodb.add_new_car(car_id,reg,engine_s)

        elif choice == "6":
            print("Countries by name")
            print("---------------------")
            country_name = input("Enter country name or part thereof:")
            countries_by_name = sarahsmysql.countries_by_name(country_name)
            for country in countries_by_name:
                print(country["Code"],"|", country["Name"], "|", country["Continent"],"|", country["Population"])
            
        elif choice == "7":
            print("Countries by population")
            print("---------------------")
            op = input("Input operator >,< or = :")
            find_population = input("Population: ")
            countries_by_pop = sarahsmysql.countries_by_population(op,find_population)
            for country in countries_by_pop:
                print(country["Code"],"|", country["Name"], "|", country["Continent"],"|", country["Population"])
            
        else: 
            print("**Error: Invalid choice. Please choose from the menu**")


if __name__ == "__main__":
    main()