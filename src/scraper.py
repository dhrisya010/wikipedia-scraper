import requests
from bs4 import BeautifulSoup
import re
from requests import Session
import json
import os
import pandas as pd


base_url = "https://country-leaders.onrender.com"
status_url = base_url + "/status"
countries_url = base_url + "/countries"
cookie_url = base_url + "/cookie"
leaders_url = base_url + "/leaders"

params = {
    "country": ""
}


#function to check the url 
def website_success():
    req = requests.get(f"{base_url}/{status_url}", params=None)
    if (req.json() == 'Alive' and req.status_code == 200):
       print(req.text)
    else:
       print(req.status_code)

# function to get cookie
def get_cookie():
   req = requests.get(f"{base_url}/{cookie_url}", params=None)
   cookie = req
   print(req.status_code)
   print(cookie.cookies)

# function to get the countries
def get_countries():
   req = requests.get(f"{base_url}/{cookie_url}", params=None)
   cookie = req
   countries = requests.get(f"{base_url}/{countries_url}", cookies=cookie.cookies)
   print(countries)


# function to get leaders
def get_leaders():
    base_url = "https://country-leaders.onrender.com"
    cookie_url = base_url + "/cookie"
    leaders_url = base_url + "/leaders"
    countries_url = base_url + "/countries"
    leaders_per_country = {}
    cookie = requests.get(cookie_url)
    countries = requests.get(countries_url, cookies=cookie.cookies).json()
    for country in countries:
        leaders_per_country[country] = requests.get(leaders_url, cookies=cookie.cookies, params={'country': country}).json()
    return leaders_per_country
leaders_per_country = get_leaders()
print(leaders_per_country)



def get_first_paragraph(wiki_url):
   
   print(wiki_url) # keep this for the rest of the notebook
   wikipedia_response = requests.get(wiki_url)   
   soup = BeautifulSoup(wikipedia_response.text, 'html.parser')

   #print(wikipedia_response.text)
   paragraphs = soup.find_all("p")
   #print(paragraphs)
   first_paragraph = ''
   for paragraph in paragraphs:
       if paragraph.find("b"):
         first_paragraph =  re.sub(r' \[.*\].*?,', ',', paragraph.get_text())
         break
   return first_paragraph


wiki_url = leaders_per_country['fr'][0]['wikipedia_url']
first_paragraph = get_first_paragraph(wiki_url)
print(first_paragraph)