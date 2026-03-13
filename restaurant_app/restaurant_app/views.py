#from django.http import HttpResponse
from django.shortcuts import render

def products_page(req):
  #  return HttpResponse("wazzzaaaaa  product")
  return  render(req,'main.html')

