from django.shortcuts import render
from FirstPage.models import *
from django.contrib.sessions.models import Session

# Create your views here.


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
