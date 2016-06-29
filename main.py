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
(5) Specific Film
(6) Specific Vehicles
"""))

#url = "http://swapi.co/api/people"
#response = requests.get(url).json()
#if choices == 4:
    # if response["next"]:
        # while response["next"]:
            # for people in response["results"]:
            #     person_id.append(people["url"].split("/")[5])
            #     person_name.append(people["name"])
            # url = response["next"]
            # response = requests.get(url).json()
        # else:
            # for people in response["results"]:
            #     person_id.append(people["url"].split("/")[5])
            #     person_name.append(people["name"])



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

if choices == 4:
    prompt = input("Please choose character (1-88): ")
    url = "http://swapi.co/api/people"
    new = ("{}/{}".format(url, prompt).strip("http://"))
    url = "http://" + new
    response = requests.get(url).json()
    print(response["name"],"\n",
    response["films"],"\n",
    response["species"],"\n",
    response["vehicles"],"\n",
    response["starships"])
    prompt = input("Would you like to search another character? y/n: ")
    if prompt == "y":
        get_specific_character()
    if prompt == "n":
            exit()

if choices == 5:
    prompt = input("Please choose film (1-7): ")
    url = "http://swapi.co/api/films"
    new = ("{}/{}".format(url, prompt).strip("http://"))
    url = "http://" + new
    response = requests.get(url).json()
    print(response["title"],"\n",
    response["episode_id"],"\n",
    response["opening_crawl"],"\n",
    response["director"],"\n",
    response["producer"],"\n",
    response["release_date"])


vehicle_count = []
if choices == 6:
    prompt = input("Please choose vehicle (1-39): ")
    url = "http://swapi.co/api/vehicles"
    new = ("{}/{}".format(url, prompt).strip("http://"))
    url = "http://" + new
    response = requests.get(url).json()
    print(response["name"], "\n",
    response["model"], "\n",
    response["manufacturer"])
