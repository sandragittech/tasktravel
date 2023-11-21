from django.http import HttpResponse
from django.shortcuts import render
from .models import Place  # Fix the import statements
from .models import People  # Fix the import statements

def demo(request):
    obj = Place.objects.all()
    b = People.objects.all()

    # name = 'CALCULATION'  # This line is commented out, so it won't affect the code.

    return render(request, 'index.html', {'result': obj, 'peop': b})



   #  return HttpResponse("Hello World")
#def about(request):
  #  return render(request,'about.templates')
#def contact(request):
  #  return HttpResponse("HI")

#def oper(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # add=x+y
    #sub=x-y
    #mul=x*y
    #div=x/y
    #return render(request,'about.templates',{'addition':add,'subtraction':sub,'multi':mul,'divi':div})