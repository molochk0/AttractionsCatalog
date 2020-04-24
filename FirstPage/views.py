from django.shortcuts import render, redirect
from FirstPage.models import *
from FirstPage.forms import CreateAttractionForm
from django.contrib.sessions.models import Session


# def main_page_anonymous(request):
#   return render(request, "mainpageAnonymous.html")

def main_page(request):
    output = Attractions.objects.all().filter(is_approved=True)
    if request.user.is_authenticated:
        session = Session.objects.get(session_key=request.session.session_key)
        uid = session.get_decoded().get('_auth_user_id')
        return render(request, "mainpageAP.html",
                      {'attractions': output, 'uid': uid})
    return render(request, "mainpageAnonymous.html",
                  {'attractions': output})


def page_create_request(request):
    args = {'form': CreateAttractionForm()}
    if request.method == 'POST':
        new_attraction = CreateAttractionForm(request.POST, request.FILES)
        if new_attraction.is_valid():
            new_attraction.save()
            return redirect('/profile')
        else:
            args['form'] = new_attraction
            return render(request, "pageCreateRequest.html", args)
    return render(request, "pageCreateRequest.html", args)


def page_profile_ap(request):
    if request.user.is_authenticated:
        session = Session.objects.get(session_key=request.session.session_key)
        uid = session.get_decoded().get('_auth_user_id')
        if User.objects.get(id=uid).is_moderator:
            return render(request, "pageMyProfileManager.html")
        return render(request, "pageMyProfileAP.html")


def filter_attr_mainpage(request):
    if request.user.is_authenticated:
        template_name = 'mainpageAP.html'
    else:
        template_name = 'mainpageAnonymous.html'
    order_by_key = 'name'
    if request.method == 'POST':
        selectSort = request.POST.get('selectSort', '')
        if selectSort == 'alphabetAZ':
            order_by_key = 'name'
        elif selectSort == 'alphabetZA':
            order_by_key = '-name'
        elif selectSort == 'markUp':
            order_by_key = ''
        elif selectSort == 'markDown':
            order_by_key = ''
        selectCity = request.POST.get('selectCity', '')
        selectType = request.POST.get('selectType', '')
        result_bd_request = Attractions.objects.all().filter(is_approved=True, type__contains=selectType,
                                                             city_name__contains=selectCity).order_by(order_by_key)
        if result_bd_request.count() == 0:
            return render(request, template_name, {'bad_result_search': 'НЕ НАШЕЛ'})
        return render(request, template_name, {'attractions': result_bd_request})


def search_attr_by_name(request):
    if request.user.is_authenticated:
        template_name = 'mainpageAP.html'
    else:
        template_name = 'mainpageAnonymous.html'
    if request.method == 'POST':
        search_attr = request.POST.get('search_attr', '')
        result_bd_request = Attractions.objects.all().filter(name__contains=search_attr, is_approved=True)
        if result_bd_request.count() == 0:
            return render(request, template_name, {'bad_result_search': 'НЕ НАШЕЛ'})
        return render(request, template_name, {'attractions': result_bd_request})


def page_users_request(request):
    if request.user.is_authenticated:
        return render(request, "pageUsersRequests.html",
                      {'attractions': Attractions.objects.all().filter(is_approved=False)})
