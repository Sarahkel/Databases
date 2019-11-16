#Sarah Scholz, G00364736
#Applied Databases Project 2019
#4.4.1, Python Program

#MongoDB Module

import pymongo

#initializes global variable
myclient = None

def connect():
    global myclient
    myclient = pymongo.MongoClient()
    myclient.admin.command('ismaster')

def find_car(engine_size):

    global myclient
    if (not myclient):
        try:
            print("Connecting the database")
            connect()
        except Exception as e:
            print("***Error***",e)
            return
    else:
        print("Database already connected")
    mydb = myclient["mongo"]
    docs = mydb["docs"]
    mongoquery = {"car.engineSize": engine_size}
    cars = docs.find(mongoquery)
    return cars

def add_new_car(car_id,reg,engine_s):
    global myclient
    if (not myclient):
        try:
            print("Connecting the database")
            connect()
        except Exception as e:
            print("***Error***",e)
            return
    else:
        print("Database already connected")
    mydb = myclient["mongo"]
    docs = mydb["docs"]
    mongoquery = {"_id": car_id, "car": {"reg": reg, "engineSize": engine_s}}
    try:
        docs.insert_one(mongoquery)
    except Exception as e:
        print(e)



