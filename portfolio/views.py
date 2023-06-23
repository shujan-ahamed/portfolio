from django.shortcuts import render

from portfolio.models import Portfolio
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')
    paginator = Paginator(portfolios, 5)
    page = request.GET.get('page')  #get the page from GET methodinside the browser
    paged_blogs = paginator.get_page(page)

    context={
        'portfolios' : paged_blogs,
    }
    return render(request, 'portfolio.html', context)

