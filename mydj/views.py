from django.http import HttpResponse
from django.shortcuts import render
from.ml import froml
import operator
def home(Request):
    return render(Request ,'index.html',)


def result(Request):
    article=Request.GET["article"]
    word_count, var_dict=froml(article)
    return render(Request, 'result.html', {'word_count' : word_count, 'article':article,'dict':var_dict})