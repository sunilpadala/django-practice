from django.http import HttpResponse
from django.shortcuts import render
from collections import OrderedDict

def testpage(request):
    for i in range(4,10):
        return HttpResponse("This is test for "+str(i)+" time")

def homepage(request):
    return render(request,"homepage.html",{"key":"This is nothing"})

def readText(request):
    return render(request,"wc_input.html")


def getWordCount(request):
    fulltext=request.GET['Full Text']
    print(fulltext)
    word_list=fulltext.split()
    word_group={}
    for word in word_list:
        if word in word_group.keys():
            word_group[word]+=1;
        else:
            word_group[word]=1;
    count=len(fulltext.split())

    string=""
    for word in word_group.keys():
        string+=word+":"+str(word_group[word])+"\n"

    string="Top 10 used words in your text are "
    od=dict(sorted(word_group.items(),key=lambda kv: kv[1], reverse=True))
    i=0
    for wrd in od.keys():
        if i<10:
            string+=wrd+","
        else:
            break
        i+=1

    return render(request,"homepage.html",{"key":fulltext,"count":count,"dict":word_group,"odict":od,"mostused":string})
