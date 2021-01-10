from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def about(request):
	return HttpResponse("This is about")


def home(request):
	return render(request, 'home.html', {'greeting':'Hello!'})


def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	count_words = len(user_text.split())
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'countwords':count_words})