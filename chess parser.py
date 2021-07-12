from bs4 import BeautifulSoup as BS 
import requests
import re

page = 1
try:
	pages = int(input("How many pages do you wanna get?: "))
except: 
	print("Pages is a number, dumbass")
	pages=1
if pages > 100: 
	print("what the hell is fricking wrong with you")
param = input("Have any keywords? (leave blank if you don't): ")
try:
	thumbnailsOn = int(input("Want thumbnails? (1 or 0): "))
except:
	print("1 OR 0 cringe man")
	thumbnailsOn = 0
print("\n")

while page <= pages and pages > 0:
	r = requests.get("https://www.chess.com/news?page=" + str(page))
	html = BS(r.content, 'html.parser')
	items = html.select('.post-preview-list-component-v5 > .post-preview-component')

	for yep in items:
		title = yep.select('.post-preview-title')
		date = yep.select('.post-preview-meta-content > span')
		author = yep.select('.post-preview-meta-username')
		thumbnail = yep.select('.post-preview-thumbnail')
		if param != "": 
			if param.lower() in title[0].text.lower():
				if thumbnailsOn >= 1:
					print("thumbnail link: " + thumbnail[0].get('srcset', 'no thumnail') + "\nname: " + title[0].text.strip() + "\ndate: " + date[0].get('title', 'no date').strip() + "\nauthor: " + author[0].text.strip() + "\n")
				else:
					print("name: " + title[0].text.strip() + "\ndate: " + date[0].get('title', 'lol, how is there no title you idiot').strip() + "\nauthor: " + author[0].text.strip() + "\n")	
		else:
			if thumbnailsOn >= 1:
				print("thumbnail link: " + thumbnail[0].get('srcset', 'no thumnail') + "\nname: " + title[0].text.strip() + "\ndate: " + date[0].get('title', 'no date').strip() + "\nauthor: " + author[0].text.strip() + "\n")
			else: 
				print("name: " + title[0].text.strip() + "\ndate: " + date[0].get('title', 'lol, how is there no title you idiot').strip() + "\nauthor: " + author[0].text.strip() + "\n")
	page +=1
