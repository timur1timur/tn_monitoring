import requests
import json
import sqlite3
from .sentimental import sentens, keyword
from .vk_config import tokenvk
import time
import re
from .dic import dict_TNA,dict_Sport,dict_Fin,dict_Kvn,dict_Adv,dict_AZS,dict_Event,dict_Vak,dict_Merch





def get_sen(data):
    sen = sentens(data[:3500])
    score = sen['documents'][-1]['score']
    return score

def get_key(data):
    key = keyword(data[:3500])
    try:
        result1 = key['documents'][-1]['keyPhrases'][0]
    except:
        result1 = "None"
    try:
        result2 = key['documents'][-1]['keyPhrases'][1]
    except:
        result2 = "None"
    try:
        result3 = key['documents'][-1]['keyPhrases'][2]
    except:
        result3 = "None"
    try:
        result4 = key['documents'][-1]['keyPhrases'][3]
    except:
        result4 = "None"
    result = str(result1) + ", " + str(result2) + ", " + str(result3) + ", " + str(result4)
    return result

def get_mark(data):
    g = data
    if g < 0.39:
        rdata = "danger"
    elif 0.39 < g < 0.52:
        rdata = "secondary"
    else:
        rdata = "success"
    return rdata

def clear_text(data):
    clear_links = re.sub(r'http\S+', '', data)
    clear_sym = re.sub(r'[^\w\s]+|[\d]+', r'', clear_links).strip()
    return clear_sym

def get_data(data, number, query):

    try:
        types = str(data[number]['post_type'])
    except:
        types = "None"

    try:
        ids = str(data[number]['id'])
    except:
        ids = "None"

    try:
        rdate = data[number]['date']
        dates = time.strftime('%Y-%m-%d %H:%M', time.localtime(rdate))
    except:
        dates = "None"

    try:
        owners = str(data[number]['owner_id'])
    except:
        owners = "None"

    try:
        texts = str(data[number]['text'])
    except:
        texts = "None"

    try:
        textsprev = texts[:200]+"..."
    except:
        textsprev = "None"
    try:
        time.sleep(1)
        score = str(round(get_sen(clear_text(texts)),2))
    except:
        score = "Нет оценки"

    try:
        time.sleep(1)
        keyw = str(get_key(clear_text(texts)))
    except:
        keyw = "None"

    try:
        replyids = str(data[number]['id'])
        postids = str(data[number]['post_id'])
    except:
        replyids = "None"
        postids = "None"

    if types == "reply":
        links = "https://vk.com/wall" + owners + "_" + postids + "?reply=" + replyids
    else:
        links = "https://vk.com/wall" + owners + "_" + ids

    try:
        marks = get_mark(float(score))
    except:
        marks = "warning"

    try:
        lens = str(len(texts))
    except:
        lens = "-"

    querys = query

    try:
        if owners[0].isdigit() is True:
            owner_types = 'User'
        else:
            owner_types = 'Group/Community'
    except:
        owner_types = "None"

    try:
        category = CheckCat(texts)
    except:
        category = 'None'

    massive = {
        'dates': dates,
        'types': types,
        'owner_types': owner_types,
        'link': links,
        'id': ids,
        'owner': owners,
        'text': texts,
        'text_prev': textsprev,
        'query': querys,
        'score': score,
        'keyword': keyw,
        'mark': marks,
        'len': lens,
        'category': category
    }
    return massive



def search_dict(text1, dict1):
    clear_sym = re.sub(r'[^\w\s]+|[\d]+', '', text1).strip()
    create_list = clear_sym.split(' ')
    result = list(set(create_list) & set(dict1))
    return len(result)

def CheckCat(text):
    if len(text) == 0:
        Multimedia = 1
        TNA = 0
        Sport = 0
        Fin = 0
        Kvn = 0
        AZS = 0
        Adv = 0
        Event = 0
        Vak = 0
        Merch = 0
        Common = 0
    else:
        Multimedia = 0
        TNA = search_dict(text, dict_TNA)
        Sport = search_dict(text, dict_Sport)
        Fin = search_dict(text, dict_Fin)
        Kvn = search_dict(text, dict_Kvn)
        AZS = search_dict(text, dict_AZS)
        Adv = search_dict(text, dict_Adv)
        Event = search_dict(text, dict_Event)
        Vak = search_dict(text, dict_Vak)
        Merch = search_dict(text, dict_Merch)
        Common = 0.9

    massive = {
        'Мультимедия': Multimedia,
        'Без категории': Common,
        'Культура/Концерты': TNA,
        'Спорт': Sport,
        'Финансы': Fin,
        'КВН': Kvn,
        'АЗС': AZS,
        'Реклама': Adv,
        'События': Event,
        'Вакансии': Vak,
        'Товары ТН': Merch
    }

    g = max(massive, key=massive.get)

    return g

def connectVK(query, count, start, end):
    token = tokenvk
    start_time = start
    end_time = end
    r = requests.get('https://api.vk.com/method/newsfeed.search', params={'q': query, 'start_time': start_time, 'end_time': end_time,'count': count, 'access_token': token, 'type': 1, 'v': 5.56})
    post = r.json()['response']['items']
    return post



#def main():
 #   hg = Prepare()['suc']
  #  print(hg)


#if __name__ == '__main__':
 #  main()
