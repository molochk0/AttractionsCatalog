from django.shortcuts import render, redirect
from Attractions_Catalog_App.FirstPage import *
from Attractions_Catalog_App.FirstPage import CreateAttractionForm
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from .filters import AtrFilter

PAGE_SIZE = 2


def main_page(request, page_number=1):
    output = Attractions.objects.all().filter(is_approved=True)
    current_page = Paginator(output, PAGE_SIZE)
    return render(request, "mainpageMain.html",
                  {'attractions': current_page.page(page_number)})


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


def filter_attr_mainpage(request, page_number=1):
    template_name = 'mainpageFilter.html'
    order_by_key = 'name'
    if request.method == 'GET':
        selectSort = request.GET.get('selectSort', '')
        if selectSort == 'alphabetAZ':
            order_by_key = 'name'
        elif selectSort == 'alphabetZA':
            order_by_key = '-name'
        elif selectSort == 'markUp':
            order_by_key = ''  #########
        elif selectSort == 'markDown':
            order_by_key = '' #########
        selectCity = request.GET.get('selectCity', '')
        selectType = request.GET.get('selectType', '')
        result_bd_request = Attractions.objects.all().filter(is_approved=True, type__contains=selectType,
                                                             city_name__contains=selectCity).order_by(order_by_key)
        if result_bd_request.count() == 0:
            return render(request, template_name, {'bad_result_search': 'НЕ НАШЕЛ'})
        current_page = Paginator(result_bd_request, PAGE_SIZE)
        return render(request, template_name,
                      {'attractions': current_page.page(page_number), 'url_bonus': 'filter', 'selectSort': selectSort,
                       'selectCity': selectCity, 'selectType': selectType})


def search_attr_by_name(request, page_number=1):
    template_name = 'mainpageSearch.html'
    if request.method == 'GET':
        search_attr = request.GET.get('search_attr', '')
        result_bd_request = Attractions.objects.all().filter(name__contains=search_attr, is_approved=True)
        if result_bd_request.count() == 0:
            return render(request, template_name, {'bad_result_search': 'НЕ НАШЕЛ'})
        current_page = Paginator(result_bd_request, PAGE_SIZE)
        return render(request, template_name, {'attractions': current_page.page(page_number), 'url_bonus': 'search',
                                               'search_attr': search_attr})


def page_users_request(request, page_number=1):
    if request.user.is_authenticated:
        result_bd_request = Attractions.objects.all().filter(is_approved=False)
        current_page = Paginator(result_bd_request, PAGE_SIZE)
        return render(request, "pageUsersRequests.html",
                      {'attractions': current_page.page(page_number), 'url_bonus': 'users_requests'})
