# Web-Scrapping-Books
The following project demonstrates the process of web scrapping, using BeautifulSoup4.

## Description
The various modules used in this project are:
  - BeautifulSoup4
  - Requests
  - csv
  
Beautiful Soup is a library that is used to scrap information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
Requests is a library that is used for making HTTP requests to web pages.

Once an response is obtained for the web page that the user wishes to scrape, it can be passed as an argument to the BeautifulSoup constructor, to create an instance of its class. This instance serves as a tree, to navigate to the various tags and its data of the web page.

## Webpage
The webpage used in this project is http://books.toscrape.com/catalogue/category/books/horror_31/index.html.
It contains a vast library of books to be bought by intrested users in various different genres.

## Objective
The goal of this project is to extract the Title, Price, Cover Page, Rating and availability of books in the Horror genre using web scrapping and store the results in a csv file for further data analytics.


