import requests
import json


movie_name = input("Enter the movie name (Press q to quit) : ")
while(movie_name != 'q'):
    movie_name = movie_name.replace(' ', '+')
    api_key = "548951f"   """this is just some random number, enter your api key from omdbapi.com here"""
    url = "http://www.omdbapi.com/?t=" + movie_name + "&apikey="+api_key
    request = requests.get(url)
    response = json.loads(request.text)
    print("\nMovie Title : " + response['Title'] + " ( " +response['Released']+" )")
    print("-------------------------------------------------------------------")
    print("Runtime: " + response['Runtime'] + "\n")
    print("Genre: " + response['Genre'] + "\n")
    print("Metacritic: " + response['Metascore'] + "/100")
    print("IMDB: " + response['imdbRating'] + "/10\n")
    print("Plot: " + response['Plot'] + "\n")
    print("Actors: " + response['Actors'] + "\n\n")
    movie_name = input("Enter the movie name (Press q to quit) : ")
