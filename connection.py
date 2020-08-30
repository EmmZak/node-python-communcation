from requests import get, post
from pprint import PrettyPrinter
from time import sleep

pp = PrettyPrinter(indent=4)

url = "http://localhost:3000/connection"
keys = ["tri", "name", "id"]

while True:
    sleep(1)
    try:
        data = get(url).json()

        # on vérifie que les clés du dict sont les bonnes
        if set(keys) == set(data.keys()):
            print("Structure keys are respected")
        else:
            print("Data structure form is not correct")
        
        if data["id"] == None:
            print("!!! Attention, Erreur deconnexion car id est None ")
            print("on ne peut pas se deco si on n'est pas co")

        print("tri - ", data["tri"])
        print("name - ", data["name"])
        print("id - ", data["id"])

    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(e)