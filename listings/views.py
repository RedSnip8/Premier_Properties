from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import bedroom_choices, price_choices, neighborhood_choice


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'listings': page_listings,
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    query_set_list = Listing.objects.order_by('-list_date')

    # Keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set_list = query_set_list.filter(
                description__icontains=keywords)

    # Neighborhood
    if 'neighborhood' in request.GET:
        neighborhood = request.GET['neighborhood']
        if neighborhood:
            query_set_list = query_set_list.filter(neighborhood__iexact=neighborhood)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_set_list = query_set_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set_list = query_set_list.filter(price__lte=price)

    context = {
        'neighborhood_choice': neighborhood_choice,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': query_set_list,
        'values': request.GET,
    }
    return render(request, 'listings/search.html', context)