import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome(executable_path=r'C:/Users/Aviral/Downloads/chromedriver.exe')

def getdata(soup):
    YOR = soup.find_all(class_='gig-wrapper card')
    desc,price,rating,user=list(),list(),list(),list()
    for i in YOR:
        desc.append(i.h3.text)
        price.append(int(i.footer.a.text.split('₹')[1].replace(',', '')))
        try:
            a,b = i.select('.rating-wrapper')[0].span.text.split('(')
            rating.append(a)
            user.append(b.strip(')'))
        except:
            rating.append('0.0')
            user.append('0')
    return desc,price,rating,user

category = 'cartoon'
url = 'https://www.fiverr.com/search/gigs?query='+category
driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')
desc,price,rating,user = getdata(soup)


with open('data.csv', 'a', encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for a, b, c, d in zip(desc,price,rating,user):
        writer.writerow([category,a,b,c,d])
