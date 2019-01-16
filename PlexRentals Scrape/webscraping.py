''' 
#
# Script: webscraping.py
# Author: Samuel Belarmino
# Date: January 9th, 2019
# Purpose: First webscraping script
#
'''


''' Things to research on: 
# - Urllib
# 
''' 
### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### THINGS TO DO: ADD URLS TO EACH PRODUCT
### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Ask the user what bot they want to look for?
counter = 0
kw = input("Do you want search all bots on Plex rentals or a specific bot?" 
			+ " If you're looking for a specific bot, type the name here: ")
print("\nLoading...")


# Begin web scraping

# URLlib = To open the web browser
from urllib.request import urlopen as uReq, Request
# Beautiful Soup = Package to parse an HTML file
from bs4 import BeautifulSoup as soup

myURL = 'https://plex.rentals/the-marketplace/'

req = Request(myURL, headers={'User-Agent': 'Mozilla/5.0'})
# Grabbing the page
uClient = uReq(req)
page_rawHTML = uClient.read()
#uClient.close()

# HTML Parses 
page_soup = soup(page_rawHTML, "html.parser")

# Grabs each product
containers = page_soup.findAll("li", {"class":"product-type-simple"})

print("\nPRODUCT || PRICE || SELLER\n")

for container in containers:
	product_title = container.a.h2.text
	if(kw.lower() in product_title.lower()):
		counter += 1
		price_container = container.findAll("span",{"class":"woocommerce-Price-amount amount"})
		product_price = price_container[0].text

		seller_container = container.findAll("div",{"class":"wcfmmp_sold_by_wrapper"})
		seller_name = seller_container[0].a.text

		print(product_title + " || " + product_price + " || " + seller_name)
	elif(kw.lower() == "all"):	
		counter += 1
		price_container = price_container = container.findAll("span",{"class":"woocommerce-Price-amount amount"})
		product_price = price_container[0].text

		seller_container = container.findAll("div",{"class":"wcfmmp_sold_by_wrapper"})
		seller_name = seller_container[0].a.text

		print(product_title + " || " + product_price + " || " + seller_name)	


print("\nFound '" + str(counter) + "' bots available today\n")		