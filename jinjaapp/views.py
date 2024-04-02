from django.shortcuts import render
def jinjaapp(request):
    return render(request,"jinjaapp.html",context={"name":"Aditya Sahu","place": "Odisha","course":'Computer science and Engineering','age':23})