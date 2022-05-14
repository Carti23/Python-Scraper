from pprint import pprint
from bs4 import BeautifulSoup
import requests
import pandas as pd
from send_email import send_email

# ROZETKS
url = requests.get('https://rozetka.com.ua/mobile-phones/c80003/producer=apple;series=113074,113077,113080,113083/#search_text=iphone+13')
# OLX
olx = requests.get('https://www.olx.ua/d/elektronika/telefony-i-aksesuary/q-iphone-13/')

# ROZETKA
sp = BeautifulSoup(url.content, 'html.parser')
# OLX
olx = BeautifulSoup(olx.content, 'html.parser')


# ROZETKA(find all elements)
title = sp.find_all('span', 'goods-tile__title')
price = sp.find_all('span', 'goods-tile__price-value')
review = sp.find_all('span', 'goods-tile__reviews-link')

# OLX(find all elements)
title1 = olx.find_all('h6', 'css-v3vynn-Text eu5v0x0')
price1 = olx.find_all('p', 'css-l0108r-Text eu5v0x0')
date = olx.find_all('p', 'css-p6wsjo-Text eu5v0x0')

# OLX(make a for loop to get all products)
title1Loop = [titles1.text for titles1 in title1]
price1Loop = [prices1.text for prices1 in price1]
dateLoop = [dates.text for dates in date]

# ROZETKA(make a for loop to get all products)
titleLoop = [titles.text for titles in title[0:5]]
priceLoop = [prices.text for prices in price[0:5]]
reviewLoop = [reviews.text for reviews in review[0:5]]

# make a data for the panda
data = {
	'Name of products':titleLoop,
	'Prices of products': priceLoop
}

# make a data for the panda
data1 = {
	'Name of products':title1Loop,
	'Prices of products': price1Loop,
	'Data Added': dateLoop
}

# make a panda cfg
df = pd.DataFrame(data, columns=[
	'Name of products',
	'Prices of products'
])

# make a panda cfg
df1 = pd.DataFrame(data1, columns=[
	'Name of products',
	'Prices of products',
	'Data Added'
])

# write data to the file(Rozetka.csv)
df.to_csv('Rozetka.csv')

# write data to the file(OLX.csv)
df1.to_csv('OLX.csv')
send_email()