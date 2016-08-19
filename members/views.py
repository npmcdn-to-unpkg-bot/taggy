from django.http import JsonResponse
from django.shortcuts import render

from django.views.decorators.http import require_POST


# Create your views here.
from members.models import Member


def new_member(request):
    return render(request, 'new-member.html')


@require_POST
def save_keypair(request):
    public_key = request.POST['public-key']
    private_key = request.POST['private-key']
    try:
        member = request.user.member
        member.private_key = private_key
        member.public_key = public_key
        member.save()
    except Member.DoesNotExist:
        # New user
        member = Member(public_key=public_key, private_key=private_key, user=request.user)
        member.save()

    return JsonResponse({'foo': 'bar'})
