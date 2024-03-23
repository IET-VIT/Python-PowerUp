import requests 
from bs4 import BeautifulSoup 
import time 

product_url = '''https://www.flipkart.com/lenovo-ideapad-3-core-i3-11th-gen\ 
			-8-gb-512-gb-ssd-windows-11-home-82h801l7in-82h802fjin-\ 
			82h802l3in-82h801lhin-thin-light-laptop/p/itm0e009f57a591b\ 
			?pid=COMG9VHHG6Q3RRJX&lid=LSTCOMG9VHHG6Q3RRJXQHPK6Q&marketplace\ 
			=FLIPKART&q=laptop&store=6bo%2Fb5g&srno=s_1_5&otracker=search\ 
			&otracker1=search&fm=productRecommendation%2FattachForSwatchProducts\ 
			&iid=66282f34-b708-4905-b834-af51e372d5c5.COMG9VHHG6Q3RRJX.SEARCH&ppt\ 
			=pp&ppn=pp&ssid=q2pdky02pc0000001668894808794&qH=312f91285e048e09'''

target_price = 35000


def check_price(): 
	# fetch webpage 
	r = requests.get(product_url) 
	# parse the html 
	soup = BeautifulSoup(r.content) 
	# extract price using class '_16Jk6d' 
	price = soup.find('div', attrs={"class": "_16Jk6d"}).text 
	# remove Rs symbol from price 
	price_without_Rs = price[1:] 
	# remove commas from price 
	price_without_comma = price_without_Rs.replace(",", "") 
	# convert price from string to int 
	int_price = int(price_without_comma) 
	return int_price 


cur_price = check_price() 
print(f"Current price is {cur_price}") 
print("We will inform you, once price of product hits out target price") 
print("Waiting...") 
while True: 
	# get current price 
	cur_price = check_price() 
	if cur_price <= target_price: 
		print(f"Its time to buy product, its current price is {cur_price}") 
		break
	# wait for 1 minute to check again 
	time.sleep(60) 
