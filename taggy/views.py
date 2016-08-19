from django.shortcuts import render, redirect
from members.models import Member


# Create your views here.
def index(request):
    try:
        member = request.user.member
        # load app
        return render(request, 'taggy-index.html')
    except Member.DoesNotExist:
        # New user
        return redirect('members:new-member')
