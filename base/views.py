from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')

# TODO: clear later
# with httpReponse
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse('Home Page')
# def room(request):
#     return HttpResponse("Room")
