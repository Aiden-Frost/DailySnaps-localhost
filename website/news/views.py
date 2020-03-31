from django.shortcuts import render,redirect
from django.template.defaulttags import register
from django.urls import reverse
from .models import  News
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='f002095de1a34265951d101aaa337c40')

source_info = {'':'','ABC News': 'abc-news', 'ABC News (AU)': 'abc-news-au', 'Aftenposten': 'aftenposten', 'Al Jazeera English': 'al-jazeera-english', 'ANSA.it': 'ansa', 'Argaam': 'argaam', 'Ars Technica': 'ars-technica', 'Ary News': 'ary-news', 'Associated Press': 'associated-press', 'Australian Financial Review': 'australian-financial-review', 'Axios': 'axios', 'BBC News': 'bbc-news', 'BBC Sport': 'bbc-sport', 'Bild': 'bild', 'Blasting News (BR)': 'blasting-news-br', 'Bleacher Report': 'bleacher-report', 'Bloomberg': 'bloomberg', 'Breitbart News': 'breitbart-news', 'Business Insider': 'business-insider', 'Business Insider (UK)': 'business-insider-uk', 'Buzzfeed': 'buzzfeed', 'CBC News': 'cbc-news', 'CBS News': 'cbs-news', 'CNBC': 'cnbc', 'CNN': 'cnn', 'CNN Spanish': 'cnn-es', 'Crypto Coins News': 'crypto-coins-news', 'Der Tagesspiegel': 'der-tagesspiegel', 'Die Zeit': 'die-zeit', 'El Mundo': 'el-mundo', 'Engadget': 'engadget', 'Entertainment Weekly': 'entertainment-weekly', 'ESPN': 'espn', 'ESPN Cric Info': 'espn-cric-info', 'Financial Post': 'financial-post', 'Focus': 'focus', 'Football Italia': 'football-italia', 'Fortune': 'fortune', 'FourFourTwo': 'four-four-two', 'Fox News': 'fox-news', 'Fox Sports': 'fox-sports', 'Globo': 'globo', 'Google News': 'google-news', 'Google News (Argentina)': 'google-news-ar', 'Google News (Australia)': 'google-news-au', 'Google News (Brasil)': 'google-news-br', 'Google News (Canada)': 'google-news-ca', 'Google News (France)': 'google-news-fr', 'Google News (India)': 'google-news-in', 'Google News (Israel)': 'google-news-is', 'Google News (Italy)': 'google-news-it', 'Google News (Russia)': 'google-news-ru', 'Google News (Saudi Arabia)': 'google-news-sa', 'Google News (UK)': 'google-news-uk', 'Göteborgs-Posten': 'goteborgs-posten', 'Gruenderszene': 'gruenderszene', 'Hacker News': 'hacker-news', 'Handelsblatt': 'handelsblatt', 'IGN': 'ign', 'Il Sole 24 Ore': 'il-sole-24-ore', 'Independent': 'independent', 'Infobae': 'infobae', 'InfoMoney': 'info-money', 'La Gaceta': 'la-gaceta', 'La Nacion': 'la-nacion', 'La Repubblica': 'la-repubblica', 'Le Monde': 'le-monde', 'Lenta': 'lenta', "L'equipe": 'lequipe', 'Les Echos': 'les-echos', 'Libération': 'liberation', 'Marca': 'marca', 'Mashable': 'mashable', 'Medical News Today': 'medical-news-today', 'MSNBC': 'msnbc', 'MTV News': 'mtv-news', 'MTV News (UK)': 'mtv-news-uk', 'National Geographic': 'national-geographic', 'National Review': 'national-review', 'NBC News': 'nbc-news', 'News24': 'news24', 'New Scientist': 'new-scientist', 'News.com.au': 'news-com-au', 'Newsweek': 'newsweek', 'New York Magazine': 'new-york-magazine', 'Next Big Future': 'next-big-future', 'NFL News': 'nfl-news', 'NHL News': 'nhl-news', 'NRK': 'nrk', 'Politico': 'politico', 'Polygon': 'polygon', 'RBC': 'rbc', 'Recode': 'recode', 'Reddit /r/all': 'reddit-r-all', 'Reuters': 'reuters', 'RT': 'rt', 'RTE': 'rte', 'RTL Nieuws': 'rtl-nieuws', 'SABQ': 'sabq', 'Spiegel Online': 'spiegel-online', 'Svenska Dagbladet': 'svenska-dagbladet', 'T3n': 't3n', 'TalkSport': 'talksport', 'TechCrunch': 'techcrunch', 'TechCrunch (CN)': 'techcrunch-cn', 'TechRadar': 'techradar', 'The American Conservative': 'the-american-conservative', 'The Globe And Mail': 'the-globe-and-mail', 'The Hill': 'the-hill', 'The Hindu': 'the-hindu', 'The Huffington Post': 'the-huffington-post', 'The Irish Times': 'the-irish-times', 'The Jerusalem Post': 'the-jerusalem-post', 'The Lad Bible': 'the-lad-bible', 'The Next Web': 'the-next-web', 'The Sport Bible': 'the-sport-bible', 'The Times of India': 'the-times-of-india', 'The Verge': 'the-verge', 'The Wall Street Journal': 'the-wall-street-journal', 'The Washington Post': 'the-washington-post', 'The Washington Times': 'the-washington-times', 'Time': 'time', 'USA Today': 'usa-today', 'Vice News': 'vice-news', 'Wired': 'wired', 'Wired.de': 'wired-de', 'Wirtschafts Woche': 'wirtschafts-woche', 'Xinhua Net': 'xinhua-net', 'Ynet': 'ynet'}

def home_page(request):
    data = newsapi.get_top_headlines(country='in',page_size=3)
    context = {'source':[],'author':[],'title':[],'description':[],'url':[],'image':[],'published':[],'content':[],'totalResults':[]}
    pos = 0
    for i in data['articles']:
        context['title'].append(i['title'])
        context['description'].append(i['description'])
        context['url'].append(i['url'])
        context['image'].append(i['urlToImage'])
        context['totalResults'].append(pos)
        pos+=1
    return render(request, "news/index.html", context)

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    data = newsapi.get_top_headlines(country='in',page_size=100)
    title_or_category = request.GET.get('title_or_category')
    source = request.GET.get('source')
    if is_valid_queryparam(title_or_category):
        data = newsapi.get_everything(q=title_or_category,page_size = 100,language='en')


    if is_valid_queryparam(source) and '-' not in source:
        if source not in source_info.values():
            final_source = source_info[source]
        else:
            final_source = source
        data = newsapi.get_everything(q=title_or_category,sources = final_source, page_size = 100,language='en')

    elif is_valid_queryparam(source) and '-' in source:
        country = source.split('-')[1]
        data = newsapi.get_top_headlines(q=title_or_category,country = country, page_size = 100)

    return data


def filter_news(request):
    final_data = filter(request)
    context = {'source':[],'author':[],'title':[],'description':[],'url':[],'image':[],'published':[],'content':[],'totalResults':[]}
    pos = 0
    for i in final_data['articles']:
        context['source'].append(i['source']['name'])
        context['author'].append(i['author'])
        context['title'].append(i['title'])
        context['description'].append(i['description'])
        context['url'].append(i['url'])
        context['image'].append(i['urlToImage'])
        context['published'].append(i['publishedAt'])
        context['content'].append(i['content'])
        context['totalResults'].append(pos)
        pos+=1
    return render(request, "news/filter_news.html", context)

@register.filter
def index_value(List,pos):
    return List[pos]
