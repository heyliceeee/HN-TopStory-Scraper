from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news") # get the response
yc_webpage = response.text # get the text

soup = BeautifulSoup(yc_webpage, "html.parser") # parse the text
articles = soup.find_all("span", class_="titleline") # find all the articles

a_tags = [article.find("a") for article in articles] # find the "a" tag in the articles

for a_tag in a_tags: # for each article
    link_article = a_tag.get("href") # get the link of the article
    text_article = a_tag.get_text() # get the title of the article
    upvote_article = a_tag.find_next("span", class_="score").get_text() # get the upvote

