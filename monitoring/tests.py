from django.test import TestCase
import re
from models import Storage as mod




#Проверка по словарю наличие мусора в тексте
def search_dict(text1, dict1):
    clear_sym = re.sub(r'[^\w\s]+|[\d]+', '', text1).strip()
    create_list = clear_sym.split(' ')
    result = list(set(create_list) & set(dict1))
    if not result:
        mark = 'normal'
        error = len(result)
    else:
        mark = 'trash'
        error = len(result)

    massive = {
        'status':   mark,
        'error':    error,
    }
    return massive


def testtt():
    last_q = mod.Storage.objects.all().filter(post_mark="danger")[:5]
    last_post = []
    net = 'vk'
    for p in last_q:
        text = p.post_text
        mark_trash = search_dict(text, dict_TNA)

        aposts = {
            'trash': mark_trash,
            'link': p.post_link,
            'score': p.post_score,
            'mark': p.post_mark,
            'keyword': p.post_keyword
        }
        last_post.append(aposts)
    print(last_post)

testtt()