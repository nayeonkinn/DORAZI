# nowplaying[200] + popular[400] + toprated[400] + upcomming[200]
# test data는 위의 갯수의 1/10 로 조절하여 설정 (추후 수정 요함)

import json
from pprint import pprint
import requests
import config

api_key = config.tmpd_api_key

url = "https://api.themoviedb.org/3/genre/movie/list?"

params = {"api_key": api_key,"language" : "ko-KR" }
genre_list = {}

response = requests.get(url, params=params, timeout=5)
data = response.json()["genres"]    
for my_data in data:
    genre_list[my_data.get('id')] =  my_data.get('name')
    
            # "model": "movies.genre",
            # "fields": {
            # "genre_code": my_data.get("id"),
            # "name": my_data.get("name")
            # }
  


movie_list = []
now_playing_url = "/3/movie/now_playing?"
popular_url = "/3/movie/popular?"
top_rated_url = "/3/movie/top_rated?"

url_list = [popular_url]
count = [70]
for idx, short_url in enumerate(url_list):
    for i in range(1,count[idx]):
        params = {
            "api_key": api_key,
            "page": i,
            "language":"ko-KR",
        }
        url = f"https://api.themoviedb.org{short_url}"
        response = requests.get(url, params=params, timeout=5)
        data = response.json()["results"]
        for json_object in data:
            genre_name = []
            genre_ids = json_object.get("genre_ids")
            for gid in genre_ids:
                genre = genre_list.get(gid)
                genre_name.append(genre)
            if json_object.get("genre_ids") and json_object.get('release_date'):
                my_object = {
                    "model": "movies.movie",
                    "fields": {
                        "movie_code": json_object.get("id"),
                        "title": json_object.get("title"),
                        "original_title": json_object.get("original_title"),
                        "genre_ids": " ".join(genre_name),
                        # "genre_ids": " ".join(genre_name),
                        "release_date": json_object.get("release_date"),
                        "popularity": json_object.get("popularity"),
                        "overview": json_object.get("overview"),
                        "poster_path": json_object.get("poster_path"),
                        "backdrop_path": json_object.get("backdrop_path"),
                        "vote_average": json_object.get("vote_average"),
                        # "vote_count": json_object.get("vote_count"),
                    }  
                }
            else:
                my_object = {
                    "model": "movies.movie",
                    "fields": {
                        "movie_code": json_object.get("id"),
                        "title": json_object.get("title"),
                        "original_title": json_object.get("original_title"),
                        "genre_ids": " ".join(genre_name),
                        # "genre_ids": " ".join(genre_name),
                        "release_date": '1999-01-01',
                        "popularity": json_object.get("popularity"),
                        "overview": json_object.get("overview"),
                        "poster_path": json_object.get("poster_path"),
                        "backdrop_path": json_object.get("backdrop_path"),
                        "vote_average": json_object.get("vote_average"),
                        # "vote_count": json_object.get("vote_count"),
                    }  
                }
            movie_list.append(my_object)
        response.close()

with open('./data/movie.json', 'w',  encoding='utf-8') as f:
    json.dump(movie_list, f, ensure_ascii = False, indent="")

with open('./data/genre.json', 'w',  encoding='utf-8') as f:
    json.dump(genre_list, f, ensure_ascii = False, indent="")
