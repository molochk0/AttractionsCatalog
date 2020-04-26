from django.shortcuts import render, redirect
from FirstPage.models import *
from django.contrib.sessions.models import Session


def page_attraction(request, id=1):
    if request.user.is_authenticated:
        return render(request, "pageAttractionAP.html", {'attraction': Attractions.objects.get(id=id)})
    return render(request, "pageAttractionAnonymous.html", {'attraction': Attractions.objects.get(id=id)})


def page_attraction_moderation(request, id=1):
    if request.user.is_authenticated:
        session = Session.objects.get(session_key=request.session.session_key)
        uid = session.get_decoded().get('_auth_user_id')
        if User.objects.get(id=uid).is_moderator:
            return render(request, "pageAttractionForModeration.html", {'attraction': Attractions.objects.get(id=id)})


def accept_request(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            accept_id = request.POST.get('accept_id', '')
            result_bd_request = Attractions.objects.filter(id=accept_id)
            result_bd_request.update(is_approved=True)
            return redirect('/users_requests/', permanent=True)


def decline_request(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            decline_id = request.POST.get('decline_id', '')
            result_bd_request = Attractions.objects.filter(id=decline_id)
            result_bd_request.delete()
            return redirect('/users_requests/', permanent=True)



def set_mark(request,  id=1):
    if request.user.is_authenticated:
        template_name = 'pageAttractionAP.html'
        session = Session.objects.get(session_key=request.session.session_key)
        uid = session.get_decoded().get('_auth_user_id')
        if request.method == 'POST':
            set_mark_atr_id = request.POST.get('set_mark_atr_id', '')
            val = request.POST.get('rating', '')
            defaults = {'value':val}
            Mark.objects.update_or_create(id_user_id=uid, id_Attraction_id=set_mark_atr_id, defaults=defaults)
            return render(request, template_name, {'attraction': Attractions.objects.get(id=id)})
