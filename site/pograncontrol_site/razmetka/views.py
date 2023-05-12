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
    marked = CaseText.objects.filter(tag__in=['marked', 'pass', 'vbros'])
    marked_cnt = len(marked)
    _all=CaseText.objects.all()
    all_cnt = len(_all)
    context = {'marked_cnt':marked_cnt, 'all_cnt':all_cnt}
    #print(CaseText.objects.order_by('?').first())
    return render(request, 'razmetka.html', context)
@login_required
def get_mes_info(request):
    username = request.user.username
    case_text = CaseText.objects.exclude(tag__in=['marked', 'pass', 'vbros', 'busy', 'delete'])
    case_text = case_text.order_by('?').first()
    CaseText.objects.filter(id = case_text.id).update(tag = 'busy', author = username)
    #serialized_data = serializers.serialize('json', case_text)
    request.session['case_text_id'] = case_text.id
    duplicate = Case.objects.filter(msg_id = case_text.msg_id, case_type = None)
    if len(duplicate) > 0:
        _duplicate_flag = 1
    else:
        _duplicate_flag = 0          
    _data = {'date' : case_text.date.strftime('%Y-%m-%d %H:%M:%S'),
            'mes_text' : case_text.text,
            'duplicate_exist' : _duplicate_flag}
    return JsonResponse(data=_data)
@login_required
def get_duplicate(request):
    case_text_id = request.session['case_text_id']
    case_text = CaseText.objects.filter(id = case_text_id).first()
    duplicate = Case.objects.filter(msg_id = case_text.msg_id, case_type = None)
    flag  = 0
    for i in duplicate:
        if str(i.age) in case_text.text and (i.kpp in case_text.text or i.country in case_text.text):
            duplicate = i
            flag = 1
    if flag == 0:
        duplicate = duplicate.first()
    _data = {
        'age' : duplicate.age,
        'cause': duplicate.cause,
        'army_other': duplicate.army_other,
        'country': duplicate.country,
        'kpp': duplicate.kpp,
        'yservice': duplicate.yservice,
        'voenk_region': duplicate.voenk_region,
        'kategoryh': duplicate.kategory_h,
        'kategoryz': duplicate.kategory_z,
        'date': duplicate.date
        }
    return JsonResponse(data=_data)
@login_required
def get_marked(request):
    marked = CaseText.objects.filter(tag__in=['marked', 'pass', 'vbros', 'delete'])
    marked_cnt = len(marked)
    _all=CaseText.objects.all()
    all_cnt = len(_all)
    _mtext = "Размечено {} сообщений из {}".format(marked_cnt, all_cnt)
    _data = {'marked_text': _mtext}
    return JsonResponse(data=_data)
@login_required
def add(request):
    if request.method == 'POST':
        username = request.user.username
        case_text_id = request.session['case_text_id']  # Получение сериализованных данных из сессии
        case_text = CaseText.objects.get(id__exact=case_text_id)
        if request.POST["age"] == '':
            _age = None
        else:
            _age = request.POST["age"]
        duplicate = Case.objects.filter(msg_id = case_text.msg_id, case_type = None, age = _age, country = request.POST["country"], cause = request.POST["cause"])
        if len(duplicate) == 0:
            case_item = Case(msg_id = case_text.msg_id, case_mes_id = case_text.id,
                             case_type = request.POST["case-type"],
                             age = _age, sex = request.POST["sex"],
                             cause = request.POST["cause"], army_relations = request.POST["army-relations"],
                             vus = request.POST["vus"], army_type = request.POST["army-type"],
                             army_sec_type = request.POST["army-sec-type"],
                             army_other = request.POST["army-other"],
                             country = request.POST["country"], kpp = request.POST["kpp"],
                             yservice = request.POST["yService"],
                             voenk_region = request.POST["voenk-region"],
                             voenk_city = request.POST["voenk-city"],
                             voenk_district = request.POST["voenk-district"],
                             kategory_h = request.POST["kategoryH"],
                             kategory_z = request.POST["kategoryZ"],
                             date = request.POST["date"][:10]
                             )
            case_item.save()
            CaseText.objects.filter(id = case_text.id).update(tag = 'marked', author = username)
        elif len(duplicate) == 1 and request.POST["case-type"] != 'success':
            print('FOUND 1 DUPLICATE')
            print(duplicate.id, duplicate.msg_id, case_text.id)
            duplicate = duplicate.first()
            Case.objects.filter(id = duplicate.id).update(case_mes_id = case_text.id,
                             case_type = request.POST["case-type"],
                             age = _age, sex = request.POST["sex"],
                             cause = request.POST["cause"], army_relations = request.POST["army-relations"],
                             vus = request.POST["vus"], army_type = request.POST["army-type"],
                             army_sec_type = request.POST["army-sec-type"],
                             army_other = request.POST["army-other"],
                             country = request.POST["country"], kpp = request.POST["kpp"],
                             yservice = request.POST["yService"],
                             voenk_region = request.POST["voenk-region"],
                             voenk_city = request.POST["voenk-city"],
                             voenk_district = request.POST["voenk-district"],
                             kategory_h = request.POST["kategoryH"],
                             kategory_z = request.POST["kategoryZ"],
                             date = request.POST["date"][:10])
            CaseText.objects.filter(id = case_text.id).update(tag = 'marked', author = username)
        else:
            print('FOUND OVER 1 DUPLICATE')
            CaseText.objects.filter(id = case_text.id).update(tag = 'manual', author = username)
        return HttpResponse('Данные успешно сохранены')
@login_required
def add_more(request):
    if request.method == 'POST':
        username = request.user.username
        case_text_id = request.session['case_text_id']  # Получение сериализованных данных из сессии
        case_text = CaseText.objects.get(id__exact=case_text_id)
        if request.POST["age"] == '':
            _age = None
        else:
            _age = request.POST["age"]
        duplicate = Case.objects.filter(msg_id = case_text.msg_id, case_type = None, age = _age, country = request.POST["country"], cause = request.POST["cause"])
        if len(duplicate) == 0:
            case_item = Case(msg_id = case_text.msg_id, case_mes_id = case_text.id,
                             case_type = request.POST["case-type"],
                             age = _age, sex = request.POST["sex"],
                             cause = request.POST["cause"], army_relations = request.POST["army-relations"],
                             vus = request.POST["vus"], army_type = request.POST["army-type"],
                             army_sec_type = request.POST["army-sec-type"],
                             army_other = request.POST["army-other"],
                             country = request.POST["country"], kpp = request.POST["kpp"],
                             yservice = request.POST["yService"],
                             voenk_region = request.POST["voenk-region"],
                             voenk_city = request.POST["voenk-city"],
                             voenk_district = request.POST["voenk-district"],
                             kategory_h = request.POST["kategoryH"],
                             kategory_z = request.POST["kategoryZ"],
                             date = request.POST["date"][:10]
                             )
            case_item.save()
        elif len(duplicate) == 1 and request.POST["case-type"] != 'success':
            print('FOUND 1 DUPLICATE')
            print(duplicate.id, duplicate.msg_id, case_text.id)
            duplicate = duplicate.first()
            Case.objects.filter(id = duplicate.id).update(case_mes_id = case_text.id,
                             case_type = request.POST["case-type"],
                             age = _age, sex = request.POST["sex"],
                             cause = request.POST["cause"], army_relations = request.POST["army-relations"],
                             vus = request.POST["vus"], army_type = request.POST["army-type"],
                             army_sec_type = request.POST["army-sec-type"],
                             army_other = request.POST["army-other"],
                             country = request.POST["country"], kpp = request.POST["kpp"],
                             yservice = request.POST["yService"],
                             voenk_region = request.POST["voenk-region"],
                             voenk_city = request.POST["voenk-city"],
                             voenk_district = request.POST["voenk-district"],
                             kategory_h = request.POST["kategoryH"],
                             kategory_z = request.POST["kategoryZ"],
                             date = request.POST["date"][:10])
        else:
            print('FOUND OVER 1 DUPLICATE')
            CaseText.objects.filter(id = case_text.id).update(tag = 'manual', author = username)
            marked = CaseText.objects.filter(tag__in=['marked', 'pass', 'vbros', 'delete'])
            marked_cnt = len(marked)
            _all=CaseText.objects.all()
            all_cnt = len(_all)
            context = {'marked_cnt':marked_cnt, 'all_cnt':all_cnt}
            #print(CaseText.objects.order_by('?').first())
            return HttpResponseBadRequest('error message')
        return HttpResponse('Данные успешно сохранены')
@login_required
def pass_mes(request):
    if request.method == 'POST':
        username = request.user.username
        case_text_id = request.session['case_text_id']  # Получение сериализованных данных из сессии
        case_text = CaseText.objects.get(id__exact=case_text_id)
        CaseText.objects.filter(id = case_text.id).update(tag = 'pass', author = username)    
        return HttpResponse('Данные успешно сохранены')
@login_required
def vbros(request):
    if request.method == 'POST':
        username = request.user.username
        case_text_id = request.session['case_text_id']  # Получение сериализованных данных из сессии
        case_text = CaseText.objects.get(id__exact=case_text_id)
        CaseText.objects.filter(id = case_text.id).update(tag = 'vbros', author = username) 
        return HttpResponse('Данные успешно сохранены')
def del_case(request):
    if request.method == 'POST':
        username = request.user.username
        case_text_id = request.session['case_text_id']  # Получение сериализованных данных из сессии
        case_text = CaseText.objects.get(id__exact=case_text_id)
        if username == 'aasmr':
            CaseText.objects.filter(id = case_text.id).delete()
        else:
            CaseText.objects.filter(id = case_text.id).update(tag = 'delete', author = username) 
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