import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = ""


def get_songs_list(date_format):
    url = f"https://www.billboard.com/charts/hot-100/{date_format}"

    response = requests.get(url)

    web_page = response.text
    # print(web_page)

    soup = BeautifulSoup(web_page, "html.parser")

    # first_title = soup.find(
    # name="li", class_="o-chart-results-list__item").getText()
    # first_title = soup.select("li .o-chart-results-list__item > h3"

    # need to optimize to get songs AND artist for better search results
    song_titles = soup.select("li .o-chart-results-list__item > h3")

    # print(song_titles)

    all_titles = [title.getText().strip() for title in song_titles]

    return all_titles

    # print(all_titles)


year = input(
    "What date would you like to pull music from? \
Please enter the date in this format (YYYY-MM-DD): "
)

songs_list = get_songs_list(year)

# Autheticate with SpotifyOauth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-public",
    )
)

# need to figure out how to get token.txt
# auth_url = input("Enter url you were redirected to: ")

current_user = sp.me()

user_id = current_user["id"]

# track = "Humble"
track_year = "2017"

track_ids = []
for song in songs_list:
    json_obj = sp.search(q=f"track:{song} year:{track_year}", type="track")
    ids = json_obj["tracks"]["items"][0]["id"]
    track_ids.append(ids)


# print(track_ids)
# print(len(track_ids))


# create playlist
sp.user_playlist_create(
    user=user_id,
    name=f"{year} Billboard 100",
    public=True,
    description="Billboard Top 100 from 06/24/2017",
)


# get playlist_id
playlists = sp.current_user_playlists()

for playlist in playlists["items"]:
    if playlist["name"] == f"{year} Billboard 100":
        playlist_id = playlist["id"]

print(playlist_id)

# pprint(playlist_id)

# add tracks to playlist
sp.playlist_add_items(playlist_id, track_ids)

print("Playlist has been created and tracks have been addedd. Please Check")

# We will test once we get authenticated
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#    track = item['track']
#    print(idx, track['artists'][0]['name'], " - ", track['name'])
