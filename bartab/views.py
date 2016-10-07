#from django.shortcuts import render
#from django.views.generic import ListView
from bartab.models import User, Item
from django.template import loader
from django.http import HttpResponse
from bartab.models import Item, User
from django.db.models.query_utils import DeferredAttribute
from decimal import Decimal

def index(request):
  all_users = User.objects.all()
  all_items = Item.objects.all()
  template = loader.get_template('bartab/bartab.html')
  context = {
	'users': all_users,
	'items': all_items
  }
  return HttpResponse(template.render(context, request))

def submit(request):
  params = request.GET
  username = params["name"]
  price = params["price"]
  qs = User.objects.all()
  qs = qs.filter(name=username)
  for e in qs:
    newTab = e.tab
  newTab += Decimal(price)
  qs = User.objects.all()
  qs = qs.filter(name=username).update(tab=newTab)
  print "new tab: "
  print newTab
