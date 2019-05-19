from django.shortcuts import render

from listings.models import Listing
from listings.choices import state_choices, price_choices, bedroom_choices
from realtors.models import Realtor
import pprint

# Create your views here.


def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listing,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    #pprint.pprint(state_choices)
    return render(request, 'pages/index.html', context)

def admin(request):
    return render(request, 'admin/base_site.html')

def about(request):
    #Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)