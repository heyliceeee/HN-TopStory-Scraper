from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news") # get the response
yc_webpage = response.text # get the text

soup = BeautifulSoup(yc_webpage, "html.parser") # parse the text
articles = soup.find_all("span", class_="titleline") # find all the articles

a_tags = [article.find("a") for article in articles] # find the "a" tag in the articles

article_titles = []
article_links = []
article_upvotes = []
for a_tag in a_tags: # for each article
    link_article = a_tag.get("href") # get the link of the article
    title_article = a_tag.get_text() # get the title of the article
    upvote_article = a_tag.find_next("span", class_="score").get_text() # get the upvote

    article_links.append(link_article) # append the link to the list
    article_titles.append(title_article) # append the title to the list
    article_upvotes.append(int(upvote_article.split()[0])) # append the upvote to the list


print(article_links)
print(article_titles)
print(article_upvotes)