from bs4 import BeautifulSoup

soup = BeautifulSoup(open('htmltest.html'))
print(soup.body.text)