#Author Gokul S. Evuri (gokul.evuri@gmail.com)

from django.shortcuts import render

import feedparser #need the lib to be installed system-wide [ToDo: Make it also work with in-app installation of lib]


from .models import Website

# Create your views here.

def index(request):
    feed_websites = Website.objects.all()
    #template = loader.get_template('rssfeed/index.html')
    #context = RequestContext(request, {'rssfeed':feed_websites,})
    feed_i = []
    feed = [] 
    #getting rss feed from all the sources in database
    for fw in feed_websites:
        #request the site for rss content
        #handle the exception
        feed_i.append(feedparser.parse(fw.web_url))
    # adding all entries to feed list
    for f in feed_i:
        for r in f.entries:
            feed.append(r)

    # sorting according to the date published
    sort(feed)
    context = {'rssfeed':feed, 'rss_websites':feed_websites}

    return render(request, 'rssfeed/index.html', context)

#Function sorts the feed items according to the date (see: Bubble sort)
def sort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j].published_parsed < items[j+1].published_parsed:
                items[j], items[j+1] = items[j+1], items[j]
