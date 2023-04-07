from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.exclude(topic_name='foot ball')
    LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length(('name').desc()))
    d={'webpages':LOW}
    return render(request,'display_webpages.html',context=d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2023-01-09')
    LOA=AccessRecord.objects.filter(date__gte='2023-04-04')
    LOA=AccessRecord.objects.filter(date__lt='2023-01-05')
    LOA=AccessRecord.objects.filter(date__lte='2023-07-03')
    
    d={'access':LOA}
    return render(request,'display_access.html',d)


