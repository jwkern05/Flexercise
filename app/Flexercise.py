import urllib.parse
import urllib.request
import json
import csv
import os
import os.path
import code

cwd = os.getcwd()
profiles = []
csv_file_path = cwd + '/data/profiles.csv'

menu = """
    Hi.

    Welcome to the Flexercise app! Where you can find your best workout!

    If new, please enter new. If returning, please enter login to see your profile information

""".format(len(profiles))

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

#Handle User Inputs

def new_profile():
    print("CREATING A USERNAME")
    username = input("What is your desired username")
    zipcode = input("What is your zip code?")
    new_profile = {
        "username": username,
        "zipcode": zipcode
    }
    print("NEW PROFILE IS", new_profile)
    profiles.append(new_profile)
    print(csv_file_path)
    csv_file=open(csv_file_path,"w") #
    csv_writer=csv.DictWriter(csv_file,fieldnames=profiles[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(profiles)
    csv_file.close()

def show_profile():
    profile = input("Please input your username.")
    csv_file=open(csv_file_path,"r") #
    csv_reader=csv.DictReader(csv_file)
    data=list(csv_reader)
    csv_file.close()
    matching_data = [data for data in data if data["username"] == profile]
    print(matching_data)
    return(matching_data[0]["zipcode"])

if chosen_operation == "New": new_profile()
elif chosen_operation == "Login": show_profile()
else:
    print("OOPS. PLEASE START OVER.")
    exit(0)

# COMPILE QUERY
# ... See Yahoo Weather API Docs!
zipcode=show_profile()
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='{0}')".format(zipcode)
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"

# ISSUE REQUEST

response = urllib.request.urlopen(yql_url).read()

# PARSE RESPONSE

raw_response = json.loads(response)
results = raw_response["query"]["results"]["channel"]
weather = results["item"]
current_weather = weather["forecast"][0]["text"]


#Output based on forecast for User
if current_weather == "Sunny" or "Mostly Sunny": print("It's sunny, go for a run!")
else: print("It's not sunny, go to a gym or a fitness class!")



#code.interact(local=locals())
