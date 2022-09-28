from songs_api import Songs


s = Songs()
try:
    s.searchSongByName('')
except:
    print('ERROR OCCURED')