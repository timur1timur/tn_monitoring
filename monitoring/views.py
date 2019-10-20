from django.shortcuts import render
from django.views.generic import View
from .models import StorageVK
from .backend import parse_tn as tnp
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .backend import stats

def index(request):

    query = "татнефть"
    count = 199
    start = 1570827600
    end = 1570914000
    i = 0
    res = tnp.connectVK(query, count, start, end)
    while i < count:
        #time.sleep(2)
        post = tnp.get_data(res, i, query)
        b = StorageVK(post_query=post['query'],
                    post_type= post['types'],
                    post_ownert= post['owner_types'],
                    post_link=post['link'],
                    post_id=post['id'],
                    post_date=post['dates'],
                    post_owner=post['owner'],
                    post_text=post['text'],
                    post_score=post['score'],
                    post_keyword=post['keyword'],
                    post_mark=post['mark'],
                    post_len=post['len'],
                    post_category=post['category'],
                    post_textp=post['text_prev'])

        b.save()
        i += 1

    warning =   len(StorageVK.objects.all().filter(post_mark="warning"))
    danger =    len(StorageVK.objects.all().filter(post_mark="danger"))
    secondary = len(StorageVK.objects.all().filter(post_mark="secondary"))
    success =   len(StorageVK.objects.all().filter(post_mark="success"))

    status_info = {
        'w':    warning,
        'd':    danger,
        'se':   secondary,
        'su':   success
    }

    context = {'status': status_info}

    return render(request, 'monitoring/index.html', context )

def posts(request):

    all_p =     len(StorageVK.objects.all())                                  #100
    warning =   len(StorageVK.objects.all().filter(post_mark="warning"))
    w_stat = round(((warning * 100)/all_p), 1)
    danger =    len(StorageVK.objects.all().filter(post_mark="danger"))
    d_stat = round(((danger * 100)/all_p), 1)
    secondary = len(StorageVK.objects.all().filter(post_mark="secondary"))
    sec_stat = round(((secondary * 100)/all_p), 1)
    success =   len(StorageVK.objects.all().filter(post_mark="success"))
    suc_stat = round(((success * 100)/all_p), 1)
    stat_post = {
        'all':          all_p,
        'success':      success,
        'suc_stat':     suc_stat,
        'secondary':    secondary,
        'sec_stat':     sec_stat,
        'danger':       danger,
        'd_stat':       d_stat,
        'warning':      warning,
        'w_stat':       w_stat
    }

    posts_qu = StorageVK.objects.all().filter(post_category="Без категории", post_type="reply")
    print(len(posts_qu))
    last_post = []
    net = 'vk'
    for p in posts_qu:
        try:
            score = float(p.post_score) * 100
        except:
            score = 0


        aposts = {
            'network': net,
            'link': p.post_link,
            'score': p.post_score,
            'mark': p.post_mark,
            'score_p': score,
            'date': p.post_date,
            'owner': p.post_owner,
            'type': p.post_type,
            'keyword': p.post_keyword,
            'trash': p.post_category,
            'len': p.post_len
        }
        last_post.append(aposts)

    context = {'last': last_post,
               'stat': stat_post}

    return render(request, 'monitoring/index3.html', context)

def post_list(request):
    date_m = stats.getWeekDay('2019-10-07')
    start_date = date_m['monday']
    end_date = date_m['sunday']
    posts = StorageVK.objects.all().filter(post_date__range=(start_date, end_date))[:10]
    stat = stats.GetStatWeek('2019-10-07')
    catW = stats.GetStatWeekCategory('2019-10-07')
    cat_name = []
    cat_stat = []
    for n in catW['cat_name']:
        cat_name.append(n)
    for s in catW['cat_stat']:
        f = (int(s)*100) / int(stat['all_post'])
        j = round(f)
        cat_stat.append(j)

    typePost = (int(stat['t_post'])*100) / int(stat['all_post'])
    typeReply = (int(stat['t_reply'])*100) / int(stat['all_post'])

    category = {
        'cat0': cat_name[0],
        'cat1': cat_name[1],
        'cat2': cat_name[2],
        'cat3': cat_name[3],
        'cat4': cat_name[4],
        'cat5': cat_name[5],
        'cat6': cat_name[6],
        'cat7': cat_name[7],
        'cat8': cat_name[8],
        'cat9': cat_name[9],
        'cat10': cat_name[10]
    }

    catStatistic = {
        'cat0': cat_stat[0],
        'cat1': cat_stat[1],
        'cat2': cat_stat[2],
        'cat3': cat_stat[3],
        'cat4': cat_stat[4],
        'cat5': cat_stat[5],
        'cat6': cat_stat[6],
        'cat7': cat_stat[7],
        'cat8': cat_stat[8],
        'cat9': cat_stat[9],
        'cat10': cat_stat[10]
    }

    catName = {
        'cat0': stats.catChange(cat_name[0], stats.catDic1),
        'cat1': stats.catChange(cat_name[1], stats.catDic1),
        'cat2': stats.catChange(cat_name[2], stats.catDic1),
        'cat3': stats.catChange(cat_name[3], stats.catDic1),
        'cat4': stats.catChange(cat_name[4], stats.catDic1),
        'cat5': stats.catChange(cat_name[5], stats.catDic1),
        'cat6': stats.catChange(cat_name[6], stats.catDic1),
        'cat7': stats.catChange(cat_name[7], stats.catDic1),
        'cat8': stats.catChange(cat_name[8], stats.catDic1),
        'cat9': stats.catChange(cat_name[9], stats.catDic1),
        'cat10': stats.catChange(cat_name[10], stats.catDic1),
    }

    typeStat = {
        'post': round(typePost),
        'reply': round(typeReply)
    }


    context = {
        'posts': posts,
        'stat': stat,
        'cat': category,
        'catItem': catStatistic,
        'catName': catName,
        'type': typeStat,

    }

    return render(request, 'monitoring/index_t.html', context)

def post_all(request):
    cont = ''
    posts = StorageVK.objects.all().filter()
    context = {
        'posts': posts,
        'con': cont,
        'count': posts.count()
    }
    return render(request, 'monitoring/p_all.html', context)

def post_danger(request):
    cont = "отрицательной"
    posts = StorageVK.objects.all().filter(post_mark="danger")
    context = {
        'posts': posts,
        'con': cont,
        'count': posts.count()
    }
    return render(request, 'monitoring/p_category.html', context)

def post_success(request):
    cont = "положительной"
    posts = StorageVK.objects.all().filter(post_mark="success")
    context = {
        'posts': posts,
        'con': cont,
        'count': posts.count()
    }
    return render(request, 'monitoring/p_category.html', context)

def post_secondary(request):
    cont = "нейтральной"
    posts = StorageVK.objects.all().filter(post_mark="secondary")
    context = {
        'posts': posts,
        'con': cont,
        'count': posts.count()
    }
    return render(request, 'monitoring/p_category.html', context)

def post_warning(request):
    cont = "Не оценненые"
    posts = StorageVK.objects.all().filter(post_mark="warning")
    context = {
        'posts': posts,
        'con': cont,
        'count': posts.count()
    }
    return render(request, 'monitoring/p_category.html', context)

def post_detail(request, slug):
    post = StorageVK.objects.get(slug__iexact=slug)
    return render(request, 'monitoring/p_detail.html', context={'post': post})

def post_category(request, category):
    link = category
    cat = stats.catChange(category, stats.catDic2)
    posts = StorageVK.objects.all().filter(post_category=cat)
    catW = stats.GetStatCategory(category)
    cat_name = []
    cat_stat = []
    for n in catW['cat_name']:
        cat_name.append(n)
    for s in catW['cat_stat']:
        cat_stat.append(s)

    category = {
        'cat0': cat_name[0],
        'cat1': cat_name[1],
        'cat2': cat_name[2],
        'cat3': cat_name[3],
        'cat4': cat_name[4],
        'cat5': cat_name[5],
        'cat6': cat_name[6],
        'cat7': cat_name[7],
        'cat8': cat_name[8],
        'cat9': cat_name[9],

    }

    catStatistic = {
        'cat0': cat_stat[0],
        'cat1': cat_stat[1],
        'cat2': cat_stat[2],
        'cat3': cat_stat[3],
        'cat4': cat_stat[4],
        'cat5': cat_stat[5],
        'cat6': cat_stat[6],
        'cat7': cat_stat[7],
        'cat8': cat_stat[8],
        'cat9': cat_stat[9],

    }

    catName = {
        'cat0': stats.catChange(cat_name[0], stats.catDic1),
        'cat1': stats.catChange(cat_name[1], stats.catDic1),
        'cat2': stats.catChange(cat_name[2], stats.catDic1),
        'cat3': stats.catChange(cat_name[3], stats.catDic1),
        'cat4': stats.catChange(cat_name[4], stats.catDic1),
        'cat5': stats.catChange(cat_name[5], stats.catDic1),
        'cat6': stats.catChange(cat_name[6], stats.catDic1),
        'cat7': stats.catChange(cat_name[7], stats.catDic1),
        'cat8': stats.catChange(cat_name[8], stats.catDic1),
        'cat9': stats.catChange(cat_name[9], stats.catDic1),

    }



    context = {
        'posts': posts,
        'name': cat,
        'count': posts.count(),
        'link': link,
        'cat': category,
        'catCount': catStatistic,
        'catName': catName
    }
    return render(request, 'monitoring/p_cat.html', context)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitoring/charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response




class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        days = stats.getWeekDayTest('2019-10-07')
        catW = stats.GetStatWeekCategory('2019-10-07')
        all = []
        suc = []
        dan = []
        sec = []
        pos = []
        rep = []
        cat_name = []
        cat_stat = []
        for d in days:
            a = stats.GetStatDay(d)['all_post']
            all.append(a)
            s = stats.GetStatDay(d)['success']
            suc.append(s)
            da = stats.GetStatDay(d)['danger']
            dan.append(da)
            se = stats.GetStatDay(d)['secondary']
            sec.append(se)
            po = stats.GetStatDay(d)['t_post']
            pos.append(po)
            rep1 = stats.GetStatDay(d)['t_reply']
            rep.append(rep1)
        for n in catW['cat_name']:
            cat_name.append(n)
        for s in catW['cat_stat']:
            cat_stat.append(s)


        labels =            [days[0], days[1], days[2], days[3], days[4], days[5], days[6]]
        week_all =          [all[0], all[1], all[2], all[3], all[4], all[5], all[6]]
        week_success =      [suc[0], suc[1], suc[2], suc[3], suc[4], suc[5], suc[6]]
        week_danger =       [dan[0], dan[1], dan[2], dan[3], dan[4], dan[5], dan[6]]
        week_secondary =    [sec[0], sec[1], sec[2], sec[3], sec[4], sec[5], sec[6]]

        week_cat_stat =     [cat_stat[0], cat_stat[1], cat_stat[2], cat_stat[3], cat_stat[4], cat_stat[5],
                             cat_stat[6], cat_stat[7], cat_stat[8], cat_stat[9], cat_stat[10]]

        week_cat_name =     [cat_name[0], cat_name[1], cat_name[2], cat_name[3], cat_name[4], cat_name[5],
                             cat_name[6], cat_name[7], cat_name[8], cat_name[9], cat_name[10]]

        week_post =         [pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6]]
        week_reply =        [rep[0], rep[1], rep[2], rep[3], rep[4], rep[5], rep[6]]



        data = {
                "labels": labels,
                "all": week_all,
                "success": week_success,
                "danger": week_danger,
                "secondary": week_secondary,
                "cat_name": week_cat_name,
                "cat_stat": week_cat_stat,
                "t_post": week_post,
                "t_reply": week_reply,

        }
        return Response(data)




def stat(request, *args, **kwargs):
    try:
        rec = stats.GetStatWeek('2019-10-09')
    except:
        rec = {
            'error': True
        }


    return JsonResponse(rec)