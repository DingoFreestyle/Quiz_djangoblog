from django.shortcuts import render

# Create your views here.
def Articles(request):
    if request.methond == "POST":
        