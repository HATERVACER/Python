from bs4 import BeautifulSoup as BS 
import requests
import webbrowser as wb
import re

page = 1
articleID = 0
articles = []
running = True

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
				articles.append(title[0].get('href', "I really suck"))
				if thumbnailsOn >= 1:
					articleID +=1
					print("thumbnail link: " + thumbnail[0].get('src', "couldn't get the thumbnail") + "\nlink:  " + title[0].get('href', "couldn't get the link") + "\nname: " + title[0].text.strip() + "\ndate: " + date[0].get('title', 'no date').strip() + "\nauthor: " + author[0].text.strip() + "\nID: " + str(articleID) + "\n")
				else:
					articleID +=1
					print("link:  " + title[0].get('href', "couldn't get the link") + "\nname: " + title[0].text.strip() + "\ndate: " + date[0].get('title', 'lol, how is there no title you idiot').strip() + "\nauthor: " + author[0].text.strip() + "\nID: " + str(articleID) + "\n")	
		else:
			articles.append(title[0].get('href', "I really suck"))
			if thumbnailsOn >= 1:
				articleID +=1
				print("thumbnail link: " + thumbnail[0].get('src', "couldn't get the thumbnail") + "\nlink:  " + title[0].get('href', "couldn't get the link") + "\nname: " + title[0].text.strip() + "\ndate: " + date[0].get('title', 'no date').strip() + "\nauthor: " + author[0].text.strip() + "\nID: " + str(articleID) + "\n")
			else: 
				articleID +=1 
				print("link:  " + title[0].get('href', "couldn't get the link") + "\nname: " + title[0].text.strip() + "\ndate: " + date[0].get('title', 'lol, how is there no title you idiot').strip() + "\nauthor: " + author[0].text.strip() + "\nID: " + str(articleID) + "\n")
	page +=1

# print(articles)

links = int(input("Do you wanna open links (1 or 0): "))

if links < 1:
	exit()
else: 
	while running:
		try:
			ID = int(input("ID of the link(0 if you're done): "))
		except: 
			ID = 0
		if ID <= 0:
			break
		else:
			wb.open(articles[ID-1])
