# Scrapping the sources of notices in the awesome podcast Mixx.io
#
# Website /
#       /YYYY/MM/DD/seo-title
#
#   You cannt get the post using /YYYY/MM/DD/ url
#   You can surf using page/#  (30 post links per page)
#   A long time ago, the site uses url.mixx.io to redirect to final url
#
#
#
#
#
# Ejemplos utilizados 
#       https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/?utm_source=blog&utm_medium=5-popular-python-libraries-web-scraping
#       https://www.aprendemachinelearning.com/ejemplo-web-scraping-python-ibex35-bolsa-valores/

# Libreries needed
import urllib.request #if you are using python3+ version, import 2
from bs4 import BeautifulSoup


#
# Return all links in the web page
def getLinksPage(page):
    mixxiopage = BeautifulSoup(page, features="lxml")
    all_links = mixxiopage.findAll("a")
    links = []
    for link in all_links:
        urlmixxio = link.get("href")
        links.append(urlmixxio)
    return links


# The root
homeMixxiourl = 'https://mixx.io/'
#page = urllib2.urlopen(wiki)
page = urllib.request.urlopen(homeMixxiourl)
homeMixxio = BeautifulSoup(page, features="lxml")
#print(homeMixxio.prettify())

all_links = homeMixxio.findAll("a")
#print(all_links)
links = []
for link in all_links:
    urlmixxio = link.get("href")
    #print(urlmixxio)    
    links.append(urlmixxio)
    if (urlmixxio.find("page")>-1):
        print("aqui: " , urlmixxio)
        print('' , urlmixxio.split("/")[-2])

print('tomalo', len(set(links)), set(links) )

#print(links)