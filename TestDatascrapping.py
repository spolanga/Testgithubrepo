import requests
from bs4 import BeautifulSoup
response= requests.get('https://news.ycombinator.com/news')
#print(response.text)
soup= BeautifulSoup(response.text,'html.parser')
#print(soup.findAll(id="score_43899028"))
title=soup.select('.titleline')
votes=soup.select('.score')
print(title,'\n',votes)
#findall will get all that is selected, and find will give only first occurance
#.titleline > a instead of .storylink
#inside soup.select(.score)here .stands for class
