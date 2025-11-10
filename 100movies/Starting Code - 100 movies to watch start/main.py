import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = (requests.get(URL)).text
soup = BeautifulSoup(response, "html.parser")
movie_tag = soup.find_all("h3",class_="title")
movie_title_reverse =[tag.get_text() for tag in movie_tag]
movie_title = movie_title_reverse[::-1]
with open("movies.txt","w") as file:
    file.write("\n".join(movie_title))