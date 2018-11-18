import urllib.request
import os
from bs4 import BeautifulSoup

url = input("URL: ")

# query the website and return the html to the variable "page"
page = urllib.request.urlopen(url)

# parses the html using beautiful soup and stores it in variable "soup"
soup = BeautifulSoup(page, "html.parser")

# finds headline, date published, byline (author), and main story text
articleHeadline = soup.find("h1", attrs={"class":"p-name"})
articlePublished = soup.find("div", attrs={"class":"dateline"})
articleByline = soup.find("div", attrs={"class":"byline"})
articleStory = soup.find("div", attrs={"class":"entry-content"})

# strip() is used to remove starting and trailing characters
headline = articleHeadline.text.strip() 
datepublished = articlePublished.text.strip()
byline = articleByline.text.strip()
story = articleStory.text.strip()

# variable for new directory
newdir = ("CHANGE THIS TO WHATEVER DIRECTORY YOU WANT TO USE" + headline)

# this creates a new sub-directory using the article headline and then moves to the new sub-dir
if not os.path.exists(newdir):
    os.makedirs(newdir)
os.chdir(newdir)

# this creates a new text file and prepares to write information
file = open("article.txt", "w")

article = [headline, datepublished, byline, story]

# this writes all items from "article" with two lines breaks between each item, then closes the file.
for item in article:
    file.write(item+"\n\n")
file.close()
