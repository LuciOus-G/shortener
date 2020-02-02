from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import short, content
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

default = 'nbSFHQRit4RNwKKyeE3IxIs15v33I5CDkKJ9Evw0dBdAilqKaFLeEQr57RKB0KHuyhBeaGM2m6spnvOsVX2xxZnimvFdXGeeK6hkOneOS0QPjrhq74GYaE3QF1jwtDh2ZwMurNL8hCk6GyoUWCPgDK'

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
