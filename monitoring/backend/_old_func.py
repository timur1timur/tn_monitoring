def write_json(data):
    with open('post.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=True)


def write_log(data, name):
    my_file = open('{}.txt'.format(name), 'w')
    my_file.write(data)
    my_file.close()


def postDB(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
    con = sqlite3.connect("vk_post.db")
    cur = con.cursor()

    cur.execute(
        "INSERT INTO vk(post_query, post_link, post_id, post_date, post_owner, post_text, post_score, post_keyword, post_mark, post_len) "
        "VALUES('" + val1 + "','" + val2 + "','" + val3 + "','" + val4 + "','" + val5 + "','" + val6 + "','" + val7 + "','" + val8 + "','" + val9 + "','" + val10 + "')")
    con.commit()
    cur.close()
    con.close()


def createDB():
    con = sqlite3.connect("vk_post.db")
    cur = con.cursor()

    cur.execute("""CREATE TABLE vk(
                                    id integer PRIMARY KEY,
                                    post_query text,
                                    post_link text,
                                    post_id text,
                                    post_date text,
                                    post_owner text,
                                    post_text text,
                                    post_score text,
                                    post_keyword text,
                                    post_mark text)""")
    con.commit()
    cur.close()
    con.close()


def read1():
    con = sqlite3.connect("vk_post.db")
    cur = con.cursor()
    # Выгрузка и формирование списка БДы
    new = []
    for i in cur.execute("SELECT * FROM vk"):
        i = str("{} {} {} {}".format(i[0], i[1], i[2], i[3]))
        new.append(i)
    # Форматирование списка для вывода
    sp = '\n'.join(new)
    # Дроп базы
    con.commit()
    cur.close()
    con.close()
    return sp



def read(name):
    con = sqlite3.connect("vk_post.db")
    cur = con.cursor()
    # Выгрузка и формирование списка БДы

    list_db = []

    for i in cur.execute("SELECT * FROM vk WHERE post_mark='" + name + "'"):
        link = str("{}".format(i[3]))
        date = str("{}".format(i[4]))
        owner = str("{}".format(i[5]))
        text = str("{}".format(i[6]))
        score = str("{}".format(i[7]))
        mark = str("{}".format(i[9]))
        massive = {'link': link,
                   'date': date,
                   'owner': owner,
                   'text': text,
                   'score': score,
                   'mark': mark
                   }
        list_db.append(massive)
    # Форматирование списка для вывода
    con.commit()
    cur.close()
    con.close()
    return list_db


def GoToBase():
    # f = createDB()
    key = "Татнефть"
    count = 50
    post = connectVK(key, count)
    i = 0
    while i < count:
        time.sleep(4)
        data_1 = get_data(post, i, key)
        try:
            # (post_query, post_link, post_id, post_date, post_owner, post_text, post_score, post_keyword, post_mark)
            postDB(data_1['query'], data_1['link'], data_1['id'], data_1['dates'], data_1['owner'], data_1['text'],
                   data_1['score'], data_1['keyword'], data_1['mark'], data_1['len'])
            print("Добавлен пост: {}".format(data_1['link']))
            # write_log(data_1[0], 'vk_success')
        except:
            print("Проблема с постом: {}".format(data_1['link']))
            # write_log(data_1[0], 'vk_problem')
        i += 1


def Prepare():
    danger = len(read("danger"))
    warning = len(read("warning"))
    secondary = len(read("secondary"))
    success = len(read("success"))
    massive = {
        'd': danger,
        'w': warning,
        'sec': secondary,
        'suc': success
    }
    return massive
