import urllib.parse
import urllib.request
import json
import csv

profiles = []

csv_file_path = "data/profile.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        profile.append(row)

def valid_username(username):
    usernames = []
    for profile in profiles:
        ids.append(profile["username"])
    while(username not in usernames):
        username = input("That username does not exist! Please try again: ")
    return username

def lookup_profile_by_username(profile_username):
    matching_profiles = [profile for profile in profiles if profile["username"] == profile_username]
    return matching_profiles [0]
    profile = lookup_profile_by_username(profile_username)

menu = """
    Hi.

    Welcome to the Flexercise app! Where you can find your best workout!

    If new, please enter new. If returning, please enter login

"""

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

def new():
    print("CREATING A USERNAME")
    username = input("What is your desired username")
    zip = input("What is your zip code?")
    new_profile = {
        "id": len(profile) + 1,
        "username": username,
        "zip": zip
    }
    print("NEW PROFILE IS", new_profile)
    profile.append(new_profile)

def show_profile():
    profile = input("Please input your username.")
    profile_username = valid_username(profile_username)
    for profile in profiles:
        profile_show = lookup_profile_by_username(profile_username)
    print("This is your username and location: ", dict(profile_show))


if chosen_operation == "new": new()
elif chosen_operation == "login": show_profile()
else: print("OOPS. PLEASE START OVER.")

# COMPILE QUERY
# ... See Yahoo Weather API Docs!

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='10019')"
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"

# ISSUE REQUEST

response = urllib.request.urlopen(yql_url).read()

# PARSE RESPONSE

raw_response = json.loads(response)
results = raw_response["query"]["results"]["channel"]
weather = results["item"]
