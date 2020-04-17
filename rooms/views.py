from django.shortcuts import render

# Create your views here.
def all_rooms(request):
    return render(request, "all_rooms")
