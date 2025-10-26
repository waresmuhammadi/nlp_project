from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")




def get_details(request):
    text = request.POST['text'];

    return JsonResponse(text, safe=False)