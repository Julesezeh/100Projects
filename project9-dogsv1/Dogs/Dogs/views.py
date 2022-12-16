import requests
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponsePermanentRedirect

#Use list class-based view to list all the breeds


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

'''
def get_details(dog_name):
    #API from api-ninjas
    api_url = f"https://api.api-ninjas.com/v1/dogs?name={dog_name}"
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    if response.status_code == requests.codes.ok:
        print(response.text)    
    else:
        print("Error:", response.status_code, response.text)
'''

def get_details(name):
    #API from api-ninjas
    api_url = api_url = f"https://api.api-ninjas.com/v1/dogs?name={name}"
    api_key = "SVfDH3VKQs52MpR67uDxxQ==uG1EROv2Mzcrhwvn"
    response = requests.get(api_url,headers={"X-Api-Key": api_key})
    if response.status_code == requests.codes.ok:
        print(response.text)    
    else:
        print("Error:", response.status_code, response.text)


def index(request):
    all_dogs = get_all_dogs()
    dawg = {'values':all_dogs[1:],'value':all_dogs[0] }
    return render(request,'index.html',context=dawg)


def details(request):
    gotten_name = request.POST.get('breed')
    simba = get_details(gotten_name)
    return HttpResponse("<div>Slimeee</div>")