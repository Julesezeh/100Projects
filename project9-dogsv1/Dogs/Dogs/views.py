import requests
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponsePermanentRedirect

#Use list class-based view to list all the breeds


"""
SYNTAX FOR CALLING api-ninjas Dogs api

name = 'golden retriever'
api_url = 'https://api.api-ninjas.com/v1/dogs?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

"""

#Function to get the names of all the dogs from the second api
def get_all_dogs():        
    response1=requests.get("https://dog.ceo/api/breeds/list/all")    
    items = response1.json()
    all_dogs = []
    for x in items['message'].items():
        if len(x[1])>0:
            for y in x[1]:
                all_dogs.append(f"{y} {x[0]}")
        else:
            all_dogs.append(f"{x[0]}")
	
    return all_dogs



def dog_details(name):
    api_url = api_url = f"https://api.api-ninjas.com/v1/dogs?name={name}"
    api_key = "SVfDH3VKQs52MpR67uDxxQ==uG1EROv2Mzcrhwvn"
    response = requests.get(api_url,headers={"X-Api-Key": api_key})


def index(request):
    pass