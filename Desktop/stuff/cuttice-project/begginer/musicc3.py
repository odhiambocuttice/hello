import sys
import json
from urllib.request import urlopen
from urllib.parse import quote_plus

    
def urlencode(search_term):
    return quote_plus(search_term)

def search_song(search_term):
    search_term = urlencode(search_term)
    #url = "https://musicbrainz.org/ws/2/release/?query="+search_term+"&fmt=json"
    root_url = "http://musicbrainz.org/ws/2/{api}?query={term}&fmt=json"
    
    url = root_url.format(api="release", term=search_term)
    
    
    d = fetch(url)
    for i in d["releases"]:
        artist = i["artist-credit"][0]["artist"]['id']["name"]
        title = i["title"]
        print(artist,title)

def search_artist(search_term):
    search_term = urlencode(search_term)
    #url = "https://musicbrainz.org/ws/2/artist/?query="+search_term+"&fmt=json"
    root_url = "http://musicbrainz.org/ws/2/{api}?query={term}&fmt=json"
    
    url = root_url.format(api="artist", term=search_term)
    
    
    d = fetch(url)
    for i in d["artists"]:
        genre = i["tags"]
        name = i["name"]
        print(name,genre)


def fetch(url):
    r = urlopen(url)
    return json.load(r)

if __name__ == "__main__":
    command = sys.argv[1]
    search_term = sys.argv[2]


    if command == "song":
        search_song(search_term)
    elif command == "artist":
        search_artist(search_term)
    else:
        print("Unknown command:" + command)
