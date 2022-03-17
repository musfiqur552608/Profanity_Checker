from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import requests
from requests.api import get
from better_profanity import profanity
from docx import Document
import docx
import os
import re

#this url for accessing api
URL = "http://127.0.0.1:8001/profanityapi/"

#this file for profan words
path = os.path.join(os.path.dirname(__file__), 'mywordlist.txt')

#this function convert the file data to text
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

#This is for homepage
def home(request):
    profanity.load_censor_words_from_file(path)
    return render(request, 'index.html')

#This is main function where we done everything for checking profan words
def check(request):
    try:
        if request.method == 'POST':
            #this segment for working with file
            if request.FILES:
                rawtext = request.FILES['filename']
                x = getText(rawtext)
                # here we checking the profanity
                final = profanity.censor(x)
                #here we count the profan words
                list = re.findall(r"\*+",final)
                num = len(list)
                if(num == 0):
                    pt='There is no profanity.!'
                    mydict = {
                    "ctext" : x,
                    "final" : final,
                    "value" : pt,
                    }
                else:    
                    mydict = {
                    "ctext" : x,
                    "final" : final,
                    "value" : num,
                    }
                json_data = json.dumps(mydict)
                # request api for post the data
                r = requests.post(url = URL, data=json_data)

                data = r.json()
            else:
                #this segment for working with text
                text = request.POST['rawtext']
                # here we checking the profanity
                final = profanity.censor(text)
                #here we count the profan words
                list = re.findall(r"\*+",final)
                num = len(list)
                if(num == 0):
                    pt='There is no profanity.!'
                    mydict = {
                    "ctext" : text,
                    "final" : final,
                    "value" : pt,
                    }
                else:   
                    mydict = {
                    "ctext" : text,
                    "final" : final,
                    "value" : num,
                    }
                json_data = json.dumps(mydict)
                # request api for post the data
                r = requests.post(url = URL, data=json_data)

                data = r.json()
            
        return render(request, 'index.html', context=mydict)
    except:
        return HttpResponse("Opps...!\nSomething else went wrong.")




