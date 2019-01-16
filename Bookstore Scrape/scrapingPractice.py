'''
#
# Webscraping Practice
# Objective: 
	- Practice webscraping
	- Webscraping with multiple pages
	- Webscraping data and outputting to HTML file
# Date: 1-13-18
# Author: Samuel Belarmino
#
'''

# URL format: http://books.toscrape.com/catalogue/page-**PAGE NUMBER**.html

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myURL = "http://books.toscrape.com/"

# Write an HTML file
f = open("scraping.html", "w")
# Set up the HTML file
html_setup = """<!DOCTYPE html>
<html>
	<head>
		<title>Scraping</title>
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
		<p class="top">Webscraping + Python</p>
 """

html_closer = """
</body>
</html>"""

f.write(html_setup)
f.close


for num in range(1,16):
	#print("\n***Page "+str(num)+"***")

	# Open the file to append
	f = open("scraping.html", "a+")
	# Form the body of the HTML file
	body = """\n<div class='page-container'>
	<p class='number'>Page: """+str(num)+"""</p>\n</div>\n\n"""
	f.write(body)
	f.close()

	# Begin webscraping 
	myURL = "http://books.toscrape.com/catalogue/page-"+str(num)+".html"

	uClient = uReq(myURL)
	rawHTML = uClient.read()
	uClient.close()

	parsedPage = soup(rawHTML, "html.parser")
	containers = parsedPage.findAll("li", {"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})

	for container in containers:
		book_title = container.h3.a["title"]

		# Get the container of the book price using findAll and strip the unecessary Strings
		price_container = container.findAll("div", {"class":"product_price"})
		stripped_text = price_container[0].text.replace("\n", "")
		stripped_text_1 = stripped_text.replace("In stock", "")
		stripped_text_2 = stripped_text_1.replace("Add to basket", "")
		stripped_final = stripped_text_2.replace(" ", "")

		book_price = stripped_final

		# Get the container for stock availability
		stock_container = container.findAll("p", {"class":"instock availability"})
		stripped = stock_container[0].text.replace("\n", "")
		stripped_fin = stripped.replace(" ", "")
		in_stock = stripped_fin

		# Open the file to append the actual information scraped
		f = open("scraping.html", "a+")
		# Form the body of the HTML file
		body = "<p class='info'>"+book_title + " | <span class='price'>" + book_price + "</span> | <span class='stock'>" + in_stock+"</span></p>\n"
		f.write(body)
		f.close()

		#print(book_title + " | " + book_price + " | " + in_stock)


f = open("scraping.html", "a+")
# Close the html		
f.write(html_closer)
f.close()