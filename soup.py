import requests
from bs4 import BeautifulSoup as BS
import csv

source = requests.get('http://books.toscrape.com/catalogue/category/books/horror_31/index.html').text
soup = BS(source, 'lxml')

f1 = open('Horror Books Scraped-1.csv', 'w', newline='')
csv_writer = csv.writer(f1)
csv_writer.writerow(['Title', 'Price', 'Cover', 'Ratings', 'In Stock'])

d_rating = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5}

for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    print(title)

    price = book.find('div', class_='product_price')
    price = price.p.text[1:]
    print(price)

    im = book.find('img', class_='thumbnail')
    image = im['src'][12:]
    image_link = 'http://books.toscrape.com/' + image
    print(image_link)

    rating = book.find('p')['class']
    rating = rating[1]
    print(d_rating[rating])

    is_in_stock = book.find('p', class_='instock availability').text
    is_in_stock = is_in_stock.split()
    is_in_stock = ' '.join(is_in_stock)   
    print(is_in_stock)
    
    csv_writer.writerow([title, price, image_link, d_rating[rating], is_in_stock])
f1.close()
