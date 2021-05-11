from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def news_of_day(request):
    date = dt.date.today()

    # Function to convert date object to find exactday
    return render(request, 'all-news/today-news.html', {"date": date,})


def past_days_news(request, past_date):

    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        raise Http404()

    if date == dt.date.today():
        return redirect(news_of_day)
    return render(request, 'all-news/past-news.html', {"date": date})


def convert_dates(dates):
    # Function weekdays number
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', ' Sunday']

    day = days[day_number]
    return day

