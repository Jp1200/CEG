import time
import requests
from selenium import webdriver

cities = ["Yucca Valley",
"Fillmoore",
"Agoura Hills",
"South Gate",
"Claremont",
"Santa Paula",
"Gardena",
"Cathedral City",
"Montery Park",
"San Bernardino",
"Diamond Bar",
"Montclair",
"Apple Valley",
"Laguna Niguel",
"San jacinto",
"Hemet",
"Camarillo",
"Laguna Woods",
"Hesperia",
"Pico Rivera",
"Laguna Hills",
"Menifee",
"Rialto",
"Covina",
"Lake Elsinore",
"Loma Linda"
]


PATH = "/Users/homepro/Development/CEG/chromedriver"

for city in cities:
	
	driver = webdriver.Chrome(PATH)
	get_first_search_result(city)
	
def get_search_term(city_name):
	city_name = city_name.lower()
	city_name = = city_name + " ca"
	return city_name


def get_first_search_result(search):
	result = driver.get(get_search_term(search))	
	result.find_element_by_id("search")	

