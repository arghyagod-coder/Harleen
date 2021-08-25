from bs4 import BeautifulSoup
import requests
import re
import urllib.request as urllib2
import os

def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)))

image_type = "Action"
# you can change the query for the image  here  
query = "Terminator 3 Movie"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/searches_sm=122&source=lnms&tbm=isch&sa=X&ei=4r_cVID3NYayoQTb4ICQBA&ved=0CAgQ_AUoAQ&biw=1242&bih=619&q="+query

print( url)
header = {'User-Agent': 'Mozilla/5.0'} 
soup = get_soup(url,header)

images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
#print images
for img in images:
  raw_img = urllib2.urlopen(img)
  print(raw_img)