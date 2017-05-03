
# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

infile  = open("track_uri.txt","r")
data = infile.readlines()
infile.close()

for i in range(2):
    track_uri = data[i].split("|")[1].split(":")[-1]
    print(track_uri)
    feature = sp.audio_features(str(track_uri))[0]
    print(feature)
    raw_input()


start = time.time()
features = sp.audio_features(tids)
for feature in features:
    print(feature)
raw_input()
delta = time.time() - start
for feature in features:
    print(json.dumps(feature, indent=4))
    print()
    analysis = sp._get(feature['analysis_url'])
    print(json.dumps(analysis, indent=4))
    print()
print ("features retrieved in %.2f seconds" % (delta,))
