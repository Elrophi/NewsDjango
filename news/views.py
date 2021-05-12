from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()

    # Function to convert date object to find exactday
    return render(request, 'all-news/today-news.html', {"date": date,})


def past_days_news(request, past_date):

    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news":news})

def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get('article')
        searched_articles = Article.search_by_title(search_term)
        message = f'{search_term}'
        return render(request, 'all-news/search.html', {'message:'message, 'articles':searched_articles})
        else:
            message = 'No term searched'
            return render(request, 'all-tech/search.html', {"message":message})
def convert_dates(dates):
    # Function weekdays number
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', ' Sunday']

    day = days[day_number]
    return day

