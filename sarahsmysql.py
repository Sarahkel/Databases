#Sarah Scholz, G00364736
#Applied Databases Project 2019
#4.4.1, Python Program

#MySQL Module

import pymysql

#initializes global variable
global dbworld
dbworld = None

  

def view_15_cities():
    db = pymysql.connect(host="localhost",user="root",password="root", db="world", cursorclass=pymysql.cursors.DictCursor)
    sql = "SELECT * FROM city LIMIT 15"

    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print('***Error***: ', e)

def cities_by_population(op,find_population):
    db = pymysql.connect(host="localhost",user="root",password="Dermot123", db="world", cursorclass=pymysql.cursors.DictCursor)

    with db:
        try:
            cursor = db.cursor()
            if op == ">":
                sql = "SELECT * FROM city WHERE population > %s"
            elif  op == "<":
                sql = "SELECT * FROM city WHERE population < %s"
            elif op == "=":
                sql = "SELECT * FROM city WHERE population = %s"
            else:
                print("***Error***: Please enter a valid operator")
                return
            cursor.execute(sql,find_population)
            return cursor.fetchall()
        except Exception as e:
            print("***Error***: ", e)


def enter_new_city(city_name,country_code,district,population):
    db = pymysql.connect(host="localhost",user="root",password="Dermot123", db="world", cursorclass=pymysql.cursors.DictCursor)
    sql = "INSERT INTO city (Name,CountryCode,District,Population) VALUES (%s,%s,%s,%s)"

    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql,(city_name,country_code,district,population))
            db.commit()
        except Exception as e:
                print("***Error***: ", e)

def countries_by_name(country_name):
    global dbworld
    if dbworld == None:
        print("Loading the DB for the first time")
        dbworld = pymysql.connect(host="localhost",user="root",password="Dermot123", db="world", cursorclass=pymysql.cursors.DictCursor)
    else:
        print("Database is already loaded")
    sql = "SELECT * FROM country WHERE name LIKE %s"

    with dbworld:
        try:
            cursor = dbworld.cursor()
            cursor.execute(sql,("%"+country_name+"%"))
            return cursor.fetchall()
        except Exception as e:
                print("***Error***: ", e)

def countries_by_population(op,find_population):
    global dbworld
    if dbworld == None:
        print("Loading the DB for the first time")
        dbworld = pymysql.connect(host="localhost",user="root",password="Dermot123", db="world", cursorclass=pymysql.cursors.DictCursor)
    else:
        print("Database is already loaded")

    with dbworld:
        try:
            cursor = dbworld.cursor()
            if op == ">":
                sql = "SELECT * FROM country WHERE population > %s"
            elif  op == "<":
                sql = "SELECT * FROM country WHERE population < %s"
            elif op == "=":
                sql = "SELECT * FROM country WHERE population = %s"
            else:
                print("***Error***: Please enter a valid operator")
                return
            cursor.execute(sql,find_population)
            return cursor.fetchall()
        except Exception as e:
            print('***Error***: ', e)
