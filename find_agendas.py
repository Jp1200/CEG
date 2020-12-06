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



def get_search_term(city_name):
	city_name = city_name.lower()
	city_name = city_name + " planning commission meeting agenda"	
	search = city_name.replace(" ", "+")
	return search


def get_first_search_result(search):
	driver.get("https://www.google.com/search?q=" + get_search_term(search))	
	search_div = driver.find_element_by_id("search")	
	if search_div:
		
		print(search_div)
		driver.quit()
		return
	else:
		driver.quit()
		return 	  

for city in cities:
	
	driver = webdriver.Chrome(PATH)
	print(get_search_term(city))
	get_first_search_result(city)



