from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, neighborhood_choice


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'neighborhood_choice': neighborhood_choice,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-job_title')

    context = {
        'realtors': realtors
    }

    return render(request, 'pages/about.html', context)

def sell(request):
  # get MVP
  mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

  context = {
    'mvp_realtors': mvp_realtors
  }

  return render(request, 'pages/sell.html', context)