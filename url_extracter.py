from newspaper import Article

url = "https://economictimes.indiatimes.com/news/politics-and-nation/pm-modi-to-address-the-nation-tomorrow/articleshow/75120833.cms"

def url_processing(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.text + " \n " + article.text

print(url_processing(url))




