# Description: This program will scrape and summarize news articles

#Import the libraries and build necessary variables
import nltk
import newspaper
from newspaper import articles

#Get the news sources
cnn_paper = newspaper.build('http://cnn.com')
fox_paper = newspaper.build('http://foxnews.com')
ind_paper = newspaper.build('http://independent.co.uk/us')

newsSrc = (cnn_paper, fox_paper, ind_paper)
collected_articles = list()
keyworded_articles = list()

save_txt = 'news_summary.txt'

#Functions to aid scraping
def crawl(source)
    source_paper = newspaper.build(source, memoize_articles.False)
    print("scrape size: " + str(source_paper.size()))
    for article in source_paper.articles:
            collected_articles.append(article)

def crawl_list(sources)
    newspapers = list()
    for source in sources:
        crawl(source)

#Program asks user for a keyword and implements the keyword
crawl_list(newsSrc)
keyWord = raw_input("Please enter any keyword(press enter to continue) ")

for articles in collected_articles:
	    if keyWord in article.url:
	    	    keyworded_articles.append(article)

print("Now writing " + str(len(keyworded_articles)) + " articles")

#Process articles into text doc
write = open(save_txt, 'w', encoding="utf-8")

for article in keyworded_articles:
	#Clean out defunct articles
	try:
		    article.download()
		    article.parse()
	except:
		    continue


#Format text doc
write.write('\n' + str(article.title))
write.write(' - ')

for author in article.authors
	    if author != article.authors[0]
	    	    writer.write(', ')

	    write.write(str(author))

article.nlp()
write.write('\n' + article.summary + '\n')

write.close()

#Open articles on web
web_open = input('Open all ' + str(len(keyworded_articles)) + ' on web?\n [Y] Yes; [N] No; ')

	web.open.lower() in ('y'):
	    webbrowser.opeb(collected_articles[0].url, new=1, autoraise=True)
	    for num in range(1, len(keyworded_articles)-1):
	    	    webbrowser.open(collected_articles[num].url, new=2)