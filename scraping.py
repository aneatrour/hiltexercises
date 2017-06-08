#geth libraries that you ned
from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

#store base URL for site

url = "https://github.com/humanitiesprogramming/scraping-corpus"

#print(url)
#print(url + "/subdomain")
#using that URL get the html
html = request.urlopen(url).read()
#print(html)
#print first 2000 characters
#print(html[:2000])
#use beautiful soup on the html that you have so you can work with it

soup = BeautifulSoup(html, 'lxml')
#print(soup)

links = soup.find_all('a'[0:10])
#print(links)
#print(soup.text[0:2000])
#find every linebreak character and replace it with a space
#print(soup.text.replace('\n', ' ')[0:1000])
#get first 2000 characters from text
text = soup.text[0:2000]
#go to page and select anything with class content
#print(soup.select(".content"))
#for link in soup.select("td.content a"):
#    print(link.text)

#grab links in td and print URLs
#links_html = soup.select('td.content a')
#urls = []
#for link in links_html:
#    url = link['href']
#    urls.append(url)
#print(urls)

#go through the soup and get td tags with a content class of having an anchor tag
links_html = soup.select('td.content a')
#make an empty list called urls
urls = []
#go through each url get rid of 'blob' and give me a link that adds the sub url to base url
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)

#creates an empty list called corpus_texts
corpus_texts = []
#for each thing in urls go through them and print the URLs first
#indicators that the program isn't dying on you if it takes a long time
for url in urls:
    print(url)
    #send an http request - getting html
    html = request.urlopen(url).read()
    #convert html into something usable -beautiful soup lxml is how to parse things
    soup = BeautifulSoup(html, "lxml")
    #soup.text gets the text from the soup, when you have it replace the newlines
    text = soup.text.replace('\n', '')
    #take the text data and add it to the corpus
    corpus_texts.append(text)
#print contents of corpus
print(corpus_texts)
