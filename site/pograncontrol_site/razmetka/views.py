from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Case, CaseText, MessagesTable

def _unique_values(query_set, field_name):
    _temp = query_set.values(field_name).distinct()
    _temp_ls = []
    for i in _temp:
        if i[field_name] != None:
            _temp_ls.append(i[field_name])
    return _temp_ls
        
def auth(request):
    return render(request, 'auth.html')

@login_required
def razmetka_page(request):
    case_text = CaseText.objects.exclude(tag__in=['marked', 'pass', 'vbros'])
    case_text = case_text.order_by('?').first()
    #serialized_data = serializers.serialize('json', case_text)
    request.session['case_text_id'] = case_text.id
    msg = MessagesTable.objects.get(id__exact=case_text.msg_id)
    marked = CaseText.objects.filter(tag__in=['marked', 'pass', 'vbros'])
    marked_cnt = len(marked)
    _all=CaseText.objects.all()
    all_cnt = len(_all)
    context = {'date': msg.datetime.strftime('%Y-%m-%d %H:%M:%S'), 'mes_text': case_text.text,
               'marked_cnt':marked_cnt, 'all_cnt':all_cnt}
    #print(CaseText.objects.order_by('?').first())
    return render(request, 'razmetka.html', context)
@login_required
def add(request):
    if request.method == 'POST':
        username = request.user.username
        case_text_id = request.session['case_text_id']  # Получение сериализованных данных из сессии
        case_text = CaseText.objects.get(id__exact=case_text_id)
        case_item = Case(msg_id = case_text[0]['msg_id'], case_mes_id = case_text[0]['id'],
                         case_type = request.POST["case-type"],
                         age = request.POST["age"], sex = request.POST["sex"],
                         cause = request.POST["cause"], army_relations = request.POST["army_relations"],
                         vus = request.POST["vus"], army_type = request.POST["army_type"],
                         army_sec_type = request.POST["army_sec_type"],
                         army_other = request.POST["army_other"],
                         country = request.POST["country"], kpp = request.POST["kpp"],
                         yservice = request.POST["yservice"],
                         voenk_region = request.POST["voenk_region"],
                         voenk_city = request.POST["voenk_city"],
                         voenk_district = request.POST["voenk_district"],
                         kategory_h = request.POST["kategory_h"],
                         kategory_z = request.POST["kategory_z"],
                         date = request.POST["date"][:10]
                         )
        case_item.save()
        CaseText.objects.filter(id = case_text.id).update(tag = 'marked', author = username)
        return HttpResponse('Данные успешно сохранены')
def autocmplt(request):
    _queryset = Case.objects.all()
    autocmplt_cause = _unique_values(_queryset, 'cause')
    autocmplt_army_relations = _unique_values(_queryset, 'army_relations')
    autocmplt_vus = _unique_values(_queryset, 'vus')
    autocmplt_army_type = _unique_values(_queryset, 'army_type')
    autocmplt_army_sec_type = _unique_values(_queryset, 'army_sec_type')
    autocmplt_army_other = _unique_values(_queryset, 'army_other')
    autocmplt_country = _unique_values(_queryset, 'country')
    autocmplt_kpp = _unique_values(_queryset, 'kpp')
    autocmplt_yService = _unique_values(_queryset, 'yservice')
    autocmplt_voenk_region = _unique_values(_queryset, 'voenk_region')
    autocmplt_voenk_city = _unique_values(_queryset, 'voenk_city')
    autocmplt_voenk_district = _unique_values(_queryset, 'voenk_district')
        
    return JsonResponse(data={
    'autocmplt_cause': autocmplt_cause,
    'autocmplt_army_relations':autocmplt_army_relations,
    'autocmplt_vus': autocmplt_vus,
    'autocmplt_army_type': autocmplt_army_type,
    'autocmplt_army_sec_type': autocmplt_army_sec_type,
    'autocmplt_army_other': autocmplt_army_other,
    'autocmplt_country': autocmplt_country,
    'autocmplt_kpp': autocmplt_kpp,
    'autocmplt_yService': autocmplt_yService,
    'autocmplt_voenk_region': autocmplt_voenk_region,
    'autocmplt_voenk_city': autocmplt_voenk_city,
    'autocmplt_voenk_district': autocmplt_voenk_district,
        })