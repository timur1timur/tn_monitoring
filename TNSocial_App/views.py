from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_url(request):
    return redirect('posts_week', permanent=True)