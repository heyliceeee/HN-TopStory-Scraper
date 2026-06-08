from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news") # get the response
yc_webpage = response.text # get the text

soup = BeautifulSoup(yc_webpage, "html.parser") # parse the text
spans = soup.find_all("span", class_="titleline") # find all the spans with the class titleline

links = [span.find("a") for span in spans] # find all the links in the spans

for link in links: # for each link
    title_article = link.get_text() # get the text of the article
    upvote_article = link.find_next("span", class_="score").get_text() # get the text of the upvote
    print(upvote_article)

