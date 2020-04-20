from bs4 import BeautifulSoup
import requests

url = "http://stackoverflow.com/"              # pass url here in which you have to find the links

for link in BeautifulSoup((requests.get(url)).text).find_all('a'):
    print(link.get('href'))