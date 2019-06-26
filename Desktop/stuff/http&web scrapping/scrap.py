
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url='https://www.djangoproject.com/'
uClient=uReq=(my_url)
page_html=uClient.read()
uClient.cloe()
page_soup=soup=(page_html, 'html.parser')

print (page_soup.h1)