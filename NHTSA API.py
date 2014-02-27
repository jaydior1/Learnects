import requests

nhsta = requests.get("http://www.nhtsa.gov/webapi/api/SafetyRatings")
count = nhsta.json["Count"]

for results in nhsta.json["Results"]:
    print results["ModelYear"]

print "--------------------------------------------------------"
print ("These are the %s model years available to choose from.") % (count)
print "--------------------------------------------------------"
year = raw_input("what year are you looking for?(1990-2015): ")
print "--------------------------------------------------------"

paramY = "/modelyear/" + year

def choose_year(paramY):
    nhstaY = requests.get(nhsta.url + paramY)
    for results in nhstaY.json["Results"]:
        print results["Make"]
    return nhstaY

nhstaY = choose_year(paramY)

print "--------------------------------------------------------"
make = raw_input("Now choose the make of car you are looking for from above: ")
print "--------------------------------------------------------"

paramMa = "/make/" + make

def choose_make(paramMa):
    nhstaMa = requests.get(nhstaY.url + paramMa)
    for results in nhstaMa.json["Results"]:
        print results["Model"]
    return nhstaMa

nhstaMa = choose_make(paramMa)

print "--------------------------------------------------------"
model = raw_input("Now choose a model from the list above: ")
print "--------------------------------------------------------"

paramMo = "/model/" + model

def choose_model(paramMo):
    nhstaMo = requests.get(nhstaMa.url + paramMo)
    for results in nhstaMo.json["Results"]:
        print "Vehicle Description: " + results["VehicleDescription"]
        print "Vehicle Id: " + str(results["VehicleId"])
    print"--------------------------------------------------------"
    return results["VehicleId"]

nhstaMo = choose_model(paramMo)

def get_ratings(nhstaMo):
    vehicleid = "/VehicleId/" + str(nhstaMo)
    ratings = requests.get(nhsta.url + vehicleid)
    for results in ratings.json["Results"]:
        for rating in results:
            print rating + ": " + str(results[rating]) 

get_ratings(nhstaMo)












    

