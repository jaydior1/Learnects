from urllib2 import urlopen
from json import load


def Choose_year(year):
    if year != "":
        apiUrl = "http://www.nhtsa.gov/webapi/api/SafetyRatings"
        outputFormat = "?format=json"
        apiParam = "/modelyear/" + year
        #Combine all three variables to make up the complete request URL
        response = urlopen(apiUrl + apiParam + outputFormat)
        return response
    else:
        apiUrl = "http://www.nhtsa.gov/webapi/api/SafetyRatings"
        outputFormat = "?format=json"
        apiParam = ""
        response = urlopen(apiUrl + apiParam + outputFormat)
        return response
    
year = str(raw_input("Choose a year(1990-2015):"))
    
#code below is only to handle JSON response object/format
#use equivalent sets of commands to handle xml response object/format
json_obj = load(Choose_year(year))


#Load the Result (vehicle collection) from the JSON response
print '------------------------------'
print '           Result			 '
print '------------------------------'
for objectCollection in json_obj['Results']:
	# Loop each vehicle in the vehicles collection
    for safetyRatingAttribute, safetyRatingValue in objectCollection.iteritems():
        print safetyRatingAttribute, ": ", safetyRatingValue


