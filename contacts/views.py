from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
  if request.method == 'POST':
    listing = request.POST['listing']
    listing_id = request.POST['listing_id']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']
    seller = request.POST['seller']

    # Dupe Check
    if request.user.is_authenticated:
      user_id = request.user.id
      if int(listing_id) >= 1:
        has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_contacted:
          messages.error(request, 'you have already submitted an inquiry for this property.')
          return redirect('/listings/'+listing_id)

    contact = Contact(
      listing=listing, listing_id=listing_id, name=name,
      email=email, phone=phone, message=message, user_id=user_id, seller=seller,
      )
    contact.save()

    # if seller == 'True':
    #   send_mail(
    #     'New Lead: ' + name,
    #     'Please reach out to ' + name + ' at '+ phone +' or ' + email + ' within 24 hours. Sign in to view more info.',
    #     'redsnip8.tester@gmail.com',
    #     [realtor_email],
    #     fail_silently=False
    #   )

    # else:
    #   send_mail(
    #     'New Inquiry: ' + listing,
    #     'There is an inquiry for ' + listing + '. Please reach out to ' +
    #     name + ' at '+ email + ' within 24 hours. Sign in to view more info.',
    #     'redsnip8.tester@gmail.com',
    #     [realtor_email],
    #     fail_silently=False
    #   )

    messages.success(request, 'Your request has been submitted, a realtor will be in contact soon!')
    if seller == 'True':
      return redirect('/sell')
    else:
      return redirect('/listings/'+listing_id)