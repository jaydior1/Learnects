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

def choose_car(nhsta, param):
    new_nhsta = requests.get(nhsta.url + param)
    for results in new_nhsta.json["Results"]:
        for car in results:
            print str(car) + ": " + str(results[car])
        print
    return new_nhsta

nhstaY = choose_car(nhsta, paramY)

print "--------------------------------------------------------"
make = raw_input("Now choose the make of car you are looking for from above: ")
print "--------------------------------------------------------"

paramMa = "/make/" + make
nhstaMa = choose_car(nhstaY, paramMa)

print "--------------------------------------------------------"
model = raw_input("Now choose a model from the list above: ")
print "--------------------------------------------------------"

paramMo = "/model/" + model

def get_vehicleid(nhsta, param):
    nhstaMo = requests.get(nhsta.url + param)
    for results in nhstaMo.json["Results"]:
        print "Vehicle Description: " + results["VehicleDescription"]
        print "Vehicle Id: " + str(results["VehicleId"])
    print"--------------------------------------------------------"
    return results["VehicleId"]

nhstaMo = "/VehicleId/" + str(get_vehicleid(nhstaMa, paramMo))
choose_car(nhsta, nhstaMo)
