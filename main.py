#rest apis
#apis(application programming interface)
from types import resolve_bases
import requests #requests something from tje internet
import json #json stands for javascript 

response = requests.get("https://randomuser.me/api")
# print(response.json())
gender = response.json()["results"][0]["gender"]
# print(gender)
title = response.json()["results"][0]["name"]["title"]
print(title)
first_name = response.json()["results"][0]["name"]["first"]
print(first_name)
last_name = response.json()["results"][0]["name"]["last"]
print(last_name)
email = response.json()["results"][0]["email"]
print(email)
phone_number = response.json()["results"][0]["phone"]
print(phone_number)
city = response.json()["results"][0]["location"]["city"]
print(city)
postal_code = response.json()["results"][0]["location"]["postcode"]
print(postal_code)
street_address = response.json()["results"][0]["location"]["street"]["number"]
print(street_address)
date_of_birth = response.json()["results"][0]["dob"]["date"]
print(date_of_birth)
login_user_name = response.json()["results"][0]["login"]["uuid"]
print(login_user_name)
regiestered_age = response.json()["results"][0]["dob"]["age"]