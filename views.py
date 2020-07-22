import operator
from django.http import HttpResponse
from django.shortcuts import render

def MainPage(request):
    return render(request,"homepage.html")

def Count(request):
    fulltext = request.GET["fulltext"]
    words = fulltext.split()
    allwords = {}
    for x in words:
        if x in allwords:
            allwords[x] += 1
        else:
            allwords[x] = 1
    sorted_dict = sorted(allwords.items(), key=operator.itemgetter(1), reverse=True)

    return render (request,"Count.html",{"words_used":fulltext,"numberofwords":len(words),"allwords":sorted_dict})

def About(request):
    return render(request,"About.html")
