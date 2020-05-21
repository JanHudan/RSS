from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

import feedparser

def index(request):
    	
	if request.GET.get("url"):

		url = request.GET["url"] #Getting URL

		feed = feedparser.parse(url) #Parsing XML data

		published_sorted = sorted(feed.entries,key=lambda entry: datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z'))

	else:

		feed = None

	if request.GET.get('sort') and feed:
    		
            sort = request.GET['sort']

            if sort == '2':
                published_sorted.reverse()
                feed['entries'] = published_sorted

            if sort == '3':
                feed['entries'] = published_sorted

	return render(request, 'rss/reader.html', {
		'feed' : feed,
		})