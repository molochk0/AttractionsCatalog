from django.shortcuts import render, redirect
from FirstPage.models import *
from django.contrib.sessions.models import Session
from django.http import Http404, HttpResponseNotFound


def page_attraction(request, id=1):
    try:
        atr = Attractions.objects.get(id=id)
    except Attractions.DoesNotExist:
        raise Http404()
    photos = Attachment.objects.all().filter(id_Attraction_id=id)
    if request.user.is_authenticated:
        return render(request, "pageAttractionAP.html", {'attraction': atr, 'photos': photos})
    return render(request, "pageAttractionAnonymous.html", {'attraction': atr, 'photos': photos})


def page_attraction_moderation(request, id=1):
    try:
        atr = Attractions.objects.get(id=id)
    except Attractions.DoesNotExist:
        raise Http404()
    photos = Attachment.objects.all().filter(id_Attraction_id=id)
    if request.user.is_authenticated:
        session = Session.objects.get(session_key=request.session.session_key)
        uid = session.get_decoded().get('_auth_user_id')
        if User.objects.get(id=uid).is_moderator:
            return render(request, "pageAttractionForModeration.html", {'attraction': atr, 'photos': photos})


def accept_request(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            accept_id = id
            try:
                result_bd_request = Attractions.objects.filter(id=accept_id)
            except Attractions.DoesNotExist:
                raise Http404()
            result_bd_request.update(is_approved=True)
            return redirect('/users_requests/', permanent=True)


def decline_request(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            decline_id = id
            try:
                result_bd_request = Attractions.objects.filter(id=decline_id)
            except Attractions.DoesNotExist:
                raise Http404()
            result_bd_request.delete()
            return redirect('/users_requests/', permanent=True)


def set_mark(request, id=1):
    try:
        atr = Attractions.objects.get(id=id)
        if request.user.is_authenticated:
            session = Session.objects.get(session_key=request.session.session_key)
            uid = session.get_decoded().get('_auth_user_id')
            if request.method == 'POST':
                val = request.POST.get('rating', '')
                defaults = {'value': val}
                Mark.objects.update_or_create(id_user_id=uid, id_Attraction_id=id, defaults=defaults)
            return redirect('/attraction/' + str(id) + '/', permanent=True)
    # except HttpResponseNotFound:
    #     raise Http404()
    except Attractions.DoesNotExist:
        raise Http404()
