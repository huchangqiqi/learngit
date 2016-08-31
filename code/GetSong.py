import os, time
import sys
import requests
from bs4 import BeautifulSoup
import threading

LUOO_URL = "http://www.luoo.net/music/{}"
MP3_URL = "http://luoo-mp3.kssws.ks-cdn.com/low/luoo/radio{}/{}.mp3"
SONG_NAME = "{}.mp3"
basePath = os.path.join(os.getcwd(), 'luowang')


def get_song_list(volumn):
    r = requests.get(LUOO_URL.format(volumn))
    bs = BeautifulSoup(r.content, 'html.parser')
    songs = bs.find_all('div', 'player-wrapper')
    print("本期歌单{}:".format(volumn))
    result = []
    for song in songs:
        meta = {}
        meta['name'] = song.find('p', 'name').getText()
        #meta['artist'] = song.find('p', 'artist').getText()
        result.append(meta)
    return result

def download_song(url,song):
    r = requests.get(url, stream=True)
    song_name = SONG_NAME.format(song['name'])
    print(song_name)
    with open(song_name, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
        fd.close()
    time.sleep(1)

def download_songs(volumn):
    songs = get_song_list(volumn)
    filename = os.path.join(basePath, str(volumn))
    if not os.path.exists(filename):
        os.makedirs(filename)
        os.chdir(filename)
    index = 0
    for song in songs:
        index += 1
        track = '%02d' % index
        url = MP3_URL.format(volumn, track)
        print("url: " + url)
        t = threading.Thread(target=download_song(url,song))
        t.start()



if __name__ == '__main__':
    vol = input()
    download_songs(vol)
