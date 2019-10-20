import datetime
import time
import instagram

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

massive555 = {
    'Без категории': 1,
    'Мультимедия': 2,
    'Культура/Концерты': 3,
    'Спорт': 4,
    'Финансы': 5,
    'КВН': 6,
    'АЗС': 7,
    'Реклама': 8,
    'События': 9,
    'Вакансии': 10,
    'Товары ТН': 11,
}

t_list = massive555.items()
f = sorted(t_list, key=lambda zn: zn[1])
label = []
data = []
for item in f:
    i = item[0]
    label.append(i)
    s = item[1]
    data.append(s)

g = 'Мультимедия'
f = label.index(g)
label.remove(label[f])
data.remove(data[f])
print(label)
print(data)