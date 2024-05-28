from django.shortcuts import render, redirect
from shorten_url.models import URL
from core import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.middleware.csrf import get_token
# Create your views here.
import re

def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https:// or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain
        r'localhost|' # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ipv6
        r'(?::\d+)?' # port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None

def index(request):
    if request.method == 'POST':
        data = request.POST
        short_url = URL.objects.filter(original_url=data['original_url'])
        print(data['original_url'])
        print(len(short_url))
        if len(short_url) != 0:
            for i in short_url:
                data = {
                    'original_url': i.original_url,
                    'shortened_url': settings.LOCAL_HOST + i.shortened_url,
                    'get_or_create': 0
                }
                i.clicks += 1
                i.save()
                return redirect('create_short_url_def', i.shortened_url)
        else:
            print('url found')
            if is_valid_url(data['original_url']):
                create_short_url = URL(
                    original_url=data['original_url']
                )
                create_short_url.save()
                data = {
                    'original_url': create_short_url.original_url,
                    'shortened_url': settings.LOCAL_HOST + create_short_url.shortened_url,
                    'get_or_create': 1
                }
                return redirect('create_short_url_def', create_short_url.shortened_url)
            else:
                return render(request, 'index', {"error": "Invalid URL"})
    return render(request, 'index.html', {"error": "Invalid URL"})

def create_short_url(request, shortened_url):
    short_url = URL.objects.get(shortened_url=shortened_url)
    data = {
        'original_url': short_url.original_url,
        'shortened_url': settings.LOCAL_HOST + short_url.shortened_url
    }
    return render(request, 'short_url.html', data)
def redirect_url(request, link):
    print('shortened_url')
    url = URL.objects.filter(shortened_url=link)
    if url.exists:
        for i in url:
            original_url = i.original_url
            return redirect(original_url)

# @method_decorator(csrf_exempt, name='dispatch')
class CreateShortUrlView(APIView):
    def post(self, request, *args, **kwargs):
        global response
        data = request.data
        url = URL.objects.filter(original_url=data['original_url'])
        if len(url) != 0:
            for i in url:
                response = {
                    'short_url': settings.LOCAL_HOST + i.shortened_url
                }
        else:
            if is_valid_url(data['original_url']):
                create_shot_url = URL(
                    original_url=data['original_url']
                )
                create_shot_url.save()
                response = {
                    'short_url': settings.LOCAL_HOST + create_shot_url.shortened_url
                }
            else:
                response = {
                    'short_url': 'Invalid URL'
                }
        return Response(data=response, status=status.HTTP_200_OK)
