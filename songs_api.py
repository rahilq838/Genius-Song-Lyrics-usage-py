import requests

class Songs:
    def __init__(self):
        print('started')

    def searchSongByName(self, searchString):
        url = "https://genius.p.rapidapi.com/search"
        headers = {
            "X-RapidAPI-Key": "2b2ecb3514msh2f2b8f2ab48c87cp1dc250jsn98871e94e613",
            "X-RapidAPI-Host": "genius.p.rapidapi.com"
        }
        querystring = {"q":searchString}
        response = requests.request("GET", url, headers=headers, params=querystring)

        if response['meta']['status']!=200:
            raise NameError("HTTP error"+str(response['meta']['status']))
        print(response.text)

    





