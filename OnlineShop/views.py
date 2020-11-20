from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import *


def home(request):
    context = {'Products': Product.objects.all(),
               'Varaints': Variant.objects.all(),
               'Brands': Brand.objects.all(),
               'Colors': Color.objects.all(),
               'Sizes': Size.objects.all()

               }

    return render(request, 'index.html', context)
