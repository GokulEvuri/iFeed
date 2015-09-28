from django.shortcuts import render

from rssfeed.models import Website

def index(request):
    feed_websites = Website.objects.all()
    print feed_websites
    context = {'rss_websites':feed_websites}
    return render(request, 'demo_rss/index.html', context)
