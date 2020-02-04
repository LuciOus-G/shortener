from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import short, content
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

default = 'dvphXjH4v2ZhdOrDS0IYMsaPweLL4bIUzVFUyDeK5VffEqH60Djp9KDijtxQmYx6Jn2CWGpTcYtm3zFi3oilT0Cuk3nexSQpPhKhdq0syDiQNUaYllp9H2YtzotzUkqVjuUXGpKtj0LZsMyPDuHoN9'

# Create your views here.
def home(request, Token=None, *args, **kwargs):
    # obj = get_object_or_404(shr, Token=Token)
    # return HttpResponse('{sc}'.format(sc=obj.longUrl))

    ctn = content.objects.all().order_by('-date')
    paginator = Paginator(ctn, 9)
    page = request.GET.get('page', 1)
    try:
        ctn = paginator.page(page)
    except PageNotAnInteger:
        ctn = paginator.page(1)
    except EmptyPage:
        ctn = paginator.page(paginator.num_pages)


    return render(request, 'home.html', {'ctn':ctn})

def article(request, slug, Token=default):
    ctn = content.objects.all().order_by('-date')
    article = content.objects.get(slug=slug)
    urls = short.objects.get(Token=Token)
    return render(request, 'article.html', {'article':article, 'ctn':ctn, 'urls':urls})

def search(request):
    query = request.GET.get('qsearch', None)
    result = content.objects.filter(Q(title__icontains=query)).order_by('-date')

    paginator = Paginator(result, 9)
    page = request.GET.get('page', 1)
    try:
        ctn = paginator.page(page)
    except PageNotAnInteger:
        ctn = paginator.page(1)
    except EmptyPage:
        ctn = paginator.page(paginator.num_pages)

    context = {
        'ctn':ctn,
        'result':result
    }

    return render (request, 'search.html', context)

def game(request):
    gameNews = content.objects.filter(category__icontains='game').order_by('-date')
    ctn = content.objects.all().order_by('-date')

    context = {
        'game':gameNews,
        'ctn':ctn
    }

    return render(request, 'game.html', context)

def crypto(request):
    cryptoNews = content.objects.filter(category__icontains='crypto').order_by('-date')
    ctn = content.objects.all().order_by('-date')

    context = {
        'crypto':cryptoNews,
        'ctn':ctn
    }

    return render(request, 'crypto.html', context)
