from ..models import StorageVK
import datetime


def GetStatWeek(date):
    network = 'vk'
    date_m = getWeekDay(date)
    start_date = date_m['monday']
    end_date = date_m['sunday']
    #stat_d = StorageVK.objects.all().filter(post_date__startswith=date).count()
    all_post = StorageVK.objects.all().filter(post_date__range=(start_date, end_date)).count()
#Status Post
    danger = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_mark="danger").count()
    secondary = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_mark="secondary").count()
    success = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_mark="success").count()
    warning = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_mark="warning").count()
#Status Type
    t_post = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_type="post").count()
    t_reply = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_type="reply").count()
#Status Category
    c_Common = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Без категории").count()
    c_Multimedia = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Мультимедия").count()
    c_TNA = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Культура/Концерты").count()
    c_Sport = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Спорт").count()
    c_Fin = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Финансы").count()
    c_Kvn = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="КВН").count()
    c_AZS = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="АЗС").count()
    c_Adv = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Реклама").count()
    c_Event = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="События").count()
    c_Vak = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Вакансии").count()
    c_Merch = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Товары ТН").count()

    massive = {
        'all_post': all_post,
        'danger': danger,
        'secondary': secondary,
        'warning': warning,
        'success': success,
        't_post': t_post,
        't_reply': t_reply,
        'c_Common': c_Common,
        'c_Multimedia': c_Multimedia,
        'c_TNA': c_TNA,
        'c_Sport': c_Sport,
        'c_Fin': c_Fin,
        'c_Kvn': c_Kvn,
        'c_AZS': c_AZS,
        'c_Adv': c_Adv,
        'c_Event': c_Event,
        'c_Vak': c_Vak,
        'c_Merch': c_Merch,
    }
    return massive

def GetStatWeekCategory(date):
    date_m = getWeekDay(date)
    start_date = date_m['monday']
    end_date = date_m['sunday']

    c_Common = StorageVK.objects.all().filter(post_date__range=(start_date, end_date),post_category="Без категории").count()
    c_Multimedia = StorageVK.objects.all().filter(post_date__range=(start_date, end_date),post_category="Мультимедия").count()
    c_TNA = StorageVK.objects.all().filter(post_date__range=(start_date, end_date),post_category="Культура/Концерты").count()
    c_Sport = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Спорт").count()
    c_Fin = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Финансы").count()
    c_Kvn = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="КВН").count()
    c_AZS = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="АЗС").count()
    c_Adv = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Реклама").count()
    c_Event = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="События").count()
    c_Vak = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Вакансии").count()
    c_Merch = StorageVK.objects.all().filter(post_date__range=(start_date, end_date), post_category="Товары ТН").count()

    massive = {
        'Без категории': c_Common,
        'Мультимедия': c_Multimedia,
        'Культура/Концерты': c_TNA,
        'Спорт': c_Sport,
        'Финансы': c_Fin,
        'КВН': c_Kvn,
        'АЗС': c_AZS,
        'Реклама': c_Adv,
        'События': c_Event,
        'Вакансии': c_Vak,
        'Товары ТН': c_Merch,
    }

    t_list = massive.items()
    f = sorted(t_list, key=lambda zn: zn[1])
    label = []
    data = []
    for item in f:
        i = item[0]
        label.append(i)
        s = item[1]
        data.append(s)

    sortCat = {
        'cat_name': label,
        'cat_stat': data
    }

    return sortCat


def GetStatDay(date):
    network = 'vk'
    all_post = StorageVK.objects.all().filter(post_date__startswith=date).count()
#Status Post
    danger = StorageVK.objects.all().filter(post_date__startswith=date, post_mark="danger").count()
    secondary = StorageVK.objects.all().filter(post_date__startswith=date, post_mark="secondary").count()
    success = StorageVK.objects.all().filter(post_date__startswith=date, post_mark="success").count()
    warning = StorageVK.objects.all().filter(post_date__startswith=date, post_mark="warning").count()
#Status Type
    t_post = StorageVK.objects.all().filter(post_date__startswith=date, post_type="post").count()
    t_reply = StorageVK.objects.all().filter(post_date__startswith=date, post_type="reply").count()
#Status Category
    c_Common = StorageVK.objects.all().filter(post_date__startswith=date, post_category="Без категории").count()
    c_Multimedia = StorageVK.objects.all().filter(post_date__startswith=date, post_category="Мультимедия").count()
    c_TNA = StorageVK.objects.all().filter(post_date__startswith=date, post_category="Культура/Концерты").count()
    c_Sport = StorageVK.objects.all().filter(post_date__startswith=date, post_category="Спорт").count()
    c_Fin = StorageVK.objects.all().filter(post_date__startswith=date, post_category="Финансы").count()
    c_Kvn = StorageVK.objects.all().filter(post_date__startswith=date, post_category="КВН").count()
    c_AZS = StorageVK.objects.all().filter(post_date__startswith=date, post_category="АЗС").count()
    c_Adv = StorageVK.objects.all().filter(post_date__startswith=date, post_category="Реклама").count()
    c_Event = StorageVK.objects.all().filter(post_date__startswith=date, post_category="События").count()
    c_Vak = StorageVK.objects.all().filter(post_date__startswith=date, post_category="Вакансии").count()
    c_Merch = StorageVK.objects.all().filter(post_date__startswith=date, post_category="Товары ТН").count()

    massive = {
        'all_post': all_post,
        'danger': danger,
        'secondary': secondary,
        'warning': warning,
        'success': success,
        't_post': t_post,
        't_reply': t_reply,
        'c_Common': c_Common,
        'c_Multimedia': c_Multimedia,
        'c_TNA': c_TNA,
        'c_Sport': c_Sport,
        'c_Fin': c_Fin,
        'c_Kvn': c_Kvn,
        'c_AZS': c_AZS,
        'c_Adv': c_Adv,
        'c_Event': c_Event,
        'c_Vak': c_Vak,
        'c_Merch': c_Merch,
    }
    return massive


def period_week():
    date = datetime.date.today()
    w1 = date - datetime.timedelta(date.weekday())
    w2 = w1 + datetime.timedelta(1)
    w3 = w1 + datetime.timedelta(2)
    w4 = w1 + datetime.timedelta(3)
    w5 = w1 + datetime.timedelta(4)
    w6 = w1 + datetime.timedelta(5)
    w7 = w1 + datetime.timedelta(6)

    massive = {
        'today': date.strftime("%Y-%m-%d"),
        'monday': w1.strftime("%Y-%m-%d"),
        'tuesday': w2.strftime("%Y-%m-%d"),
        'wednesday': w3.strftime("%Y-%m-%d"),
        'thursday': w4.strftime("%Y-%m-%d"),
        'friday': w5.strftime("%Y-%m-%d"),
        'saturday': w6.strftime("%Y-%m-%d"),
        'sunday': w7.strftime("%Y-%m-%d"),
    }

    return massive

def getWeekDay(date):
    date1 = datetime.datetime.strptime(date, "%Y-%m-%d")
    w1 = date1 - datetime.timedelta(date1.weekday())
    w2 = w1 + datetime.timedelta(1)
    w3 = w1 + datetime.timedelta(2)
    w4 = w1 + datetime.timedelta(3)
    w5 = w1 + datetime.timedelta(4)
    w6 = w1 + datetime.timedelta(5)
    w7 = w1 + datetime.timedelta(6)

    massive = {
        'monday': w1.strftime("%Y-%m-%d"),
        'tuesday': w2.strftime("%Y-%m-%d"),
        'wednesday': w3.strftime("%Y-%m-%d"),
        'thursday': w4.strftime("%Y-%m-%d"),
        'friday': w5.strftime("%Y-%m-%d"),
        'saturday': w6.strftime("%Y-%m-%d"),
        'sunday': w7.strftime("%Y-%m-%d"),
    }

    return massive

def getWeekDayTest(date):
    date1 = datetime.datetime.strptime(date, "%Y-%m-%d")
    w1 = date1 - datetime.timedelta(date1.weekday())
    w2 = w1 + datetime.timedelta(1)
    w3 = w1 + datetime.timedelta(2)
    w4 = w1 + datetime.timedelta(3)
    w5 = w1 + datetime.timedelta(4)
    w6 = w1 + datetime.timedelta(5)
    w7 = w1 + datetime.timedelta(6)

    massive = [w1.strftime("%Y-%m-%d"),w2.strftime("%Y-%m-%d"),w3.strftime("%Y-%m-%d"),w4.strftime("%Y-%m-%d"),w5.strftime("%Y-%m-%d"),w6.strftime("%Y-%m-%d"),w7.strftime("%Y-%m-%d"),]

    return massive


def period_month():
    start = datetime.date.today()
    middle = start.day - 1
    end = start - datetime.timedelta(middle)
    delta = start - end  # as timedelta
    days = []
    for i in range(delta.days + 1):
        day = end + datetime.timedelta(days=i)
        days.append(day.strftime("%Y-%m-%d"))
    return days


def catChange(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter



catDic1 = {
    'Без категории': 'c_Common',
    'Мультимедия': 'c_Multimedia',
    'Культура/Концерты': 'c_TNA',
    'Спорт': 'c_Sport',
    'Финансы': 'c_Fin',
    'КВН': 'c_Kvn',
    'АЗС': 'c_AZS',
    'Реклама': 'c_Adv',
    'События': 'c_Event',
    'Вакансии': 'c_Vak',
    'Товары ТН': 'c_Merch',
}

catDic2 = {
    'c_Common':             'Без категории',
    'c_Multimedia':         'Мультимедия',
    'c_TNA':                'Культура/Концерты',
    'c_Sport':              'Спорт',
    'c_Fin':                'Финансы',
    'c_Kvn':                'КВН',
    'c_AZS':                'АЗС',
    'c_Adv':                'Реклама',
    'c_Event':              'События',
    'c_Vak':                'Вакансии',
    'c_Merch':              'Товары ТН',
}


def GetStatCategory(category):

    change = catChange(category, catDic2)

    c_Common = StorageVK.objects.all().filter(post_category="Без категории").count()
    c_Multimedia = StorageVK.objects.all().filter(post_category="Мультимедия").count()
    c_TNA = StorageVK.objects.all().filter(post_category="Культура/Концерты").count()
    c_Sport = StorageVK.objects.all().filter(post_category="Спорт").count()
    c_Fin = StorageVK.objects.all().filter(post_category="Финансы").count()
    c_Kvn = StorageVK.objects.all().filter(post_category="КВН").count()
    c_AZS = StorageVK.objects.all().filter(post_category="АЗС").count()
    c_Adv = StorageVK.objects.all().filter(post_category="Реклама").count()
    c_Event = StorageVK.objects.all().filter(post_category="События").count()
    c_Vak = StorageVK.objects.all().filter(post_category="Вакансии").count()
    c_Merch = StorageVK.objects.all().filter(post_category="Товары ТН").count()

    massive = {
        'Без категории': c_Common,
        'Мультимедия': c_Multimedia,
        'Культура/Концерты': c_TNA,
        'Спорт': c_Sport,
        'Финансы': c_Fin,
        'КВН': c_Kvn,
        'АЗС': c_AZS,
        'Реклама': c_Adv,
        'События': c_Event,
        'Вакансии': c_Vak,
        'Товары ТН': c_Merch,
    }

    t_list = massive.items()
    f = sorted(t_list, key=lambda zn: zn[1])
    label = []
    data = []
    for item in f:
        i = item[0]
        label.append(i)
        s = item[1]
        data.append(s)

    f = label.index(change)

    label.remove(label[f])
    data.remove(data[f])


    sortCat = {
        'cat_name': label,
        'cat_stat': data,
    }

    return sortCat