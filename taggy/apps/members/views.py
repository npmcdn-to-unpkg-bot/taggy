from django.shortcuts import render


# Create your views here.
def new_member(request):
    return render(request, 'new-member.html')
