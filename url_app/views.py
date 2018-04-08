from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import UrlShortener
from django.views import View
from .forms import NewShortLink
from django import forms
from .utils import create_shortcode
# Create your views here.
def index(request,shortcode=None):
    obj = get_object_or_404(UrlShortener,shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

class HomeView(View):
    def get(self,request,*args,**kwargs):
        form = NewShortLink()
        return render(request,'url_app/home.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form = NewShortLink(request.POST)
        user_url = request.POST['url']
        user_shortcode = request.POST['shortcode']
        if user_shortcode is None or user_shortcode is '':
            user_shortcode = create_shortcode(12)
            UrlShortener.objects.get_or_create(url=user_url,shortcode=user_shortcode)
            user_data = '127.0.0.1:8000/'+user_shortcode
            return render(request,'url_app/latest.html',{'short_url':user_data})
        else:
            sc_exists = UrlShortener.objects.filter(shortcode=user_shortcode).exists()
            if not sc_exists:
                UrlShortener.objects.get_or_create(url=user_url,shortcode=user_shortcode)
                user_data = '127.0.0.1:8000/'+user_shortcode
                return render(request,'url_app/latest.html',{'short_url':user_data})
        return render(request,'url_app/home.html',{'form':form})
