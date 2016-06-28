import requests



headers = {
    'cache-control': "no-cache",
    'postman-token': "ceefe358-8eed-6b5a-0aec-5f84b2f2ca26"
    }



choices = int(input("""
(1) Characters
(2) Films
(3) Vehicles
(4) Specific Character
"""))




url = "http://swapi.co/api/people"
response = requests.get(url).json()
if choices == 1:
    if response["next"]:
        while response["next"]:
            for people in response["results"]:
                print(people["name"])
            url = response["next"]
            response = requests.get(url).json()
            prompt = input("Would you like to see more data? y/n: ")
            if prompt == "y":
                continue
            if prompt == "n":
                break
        else:
            for people in response["results"]:
                print(people["name"])


url = "http://swapi.co/api/films"
response = requests.get(url).json()
if choices == 2:
    for films in response["results"]:
        print(films["url"].split("/")[5])
        print(films["title"])


url = "http://swapi.co/api/vehicles"
response = requests.get(url).json()
if choices == 3:
    if response["next"]:
        while response["next"]:
            for vehicles in response["results"]:
                print(vehicles["name"])
            url = response["next"]
            response = requests.get(url).json()
            prompt = input("Would you like to see more data? y/n: ")
            if prompt == "y":
                continue
            if prompt == "n":
                break
        else:
            for vehicles in response["results"]:
                print(vehicles["name"])
person_id = []
person_name = []

def get_specific_character():
    url = "http://swapi.co/api/people"
    response = requests.get(url).json()
    if choices == 4:
        if response["next"]:
            while response["next"]:
                for people in response["results"]:
                    person_id.append(people["url"].split("/")[5])
                    person_name.append(people["name"])
                url = response["next"]
                response = requests.get(url).json()
            else:
                for people in response["results"]:
                    person_id.append(people["url"].split("/")[5])
                    person_name.append(people["name"])
        prompt = input("Please type character number (1-88): ")
        url = "http://swapi.co/api/people"
        new = ("{}/{}".format(url, prompt).strip("http://"))
        url = "http://" + new
        response = requests.get(url).json()
        print(response["name"], response["species"], response["vehicles"], response["starships"])
        prompt = input("Would you like to search another character? y/n: ")
        if prompt == "y":
            get_specific_character()
        if prompt == "n":
            exit()

get_specific_character()
