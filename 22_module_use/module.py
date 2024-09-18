import datetime



def hello() :
    print("Hello! world")
    name = input("名前を入力してください:")
    print(f"Hello! {name}. Nice to meet you! ")

def info() :
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    toyear = int(now.strftime('%Y'))
    today = int(now.strftime('%m%d'))

    birthday = int(input("誕生日を入力してください(yyyyMMDD)"))

    birth_year = int(str(birthday)[0:4])
    birth_day = int(str(birthday)[4:9]) 
    diff_year = toyear - birth_year
    diff_day = today - birth_day
    print(diff_year , diff_day)
    
    age = diff_year
    if diff_day == 0 or (diff_day > 0 and birth_day > 331) :
        age = diff_year + 1
    elif diff_day < 0 :
        age = diff_year - 1

    print(f"あなたの誕生日は、{birth_year}年{str(birthday)[4:6]}月{str(birthday)[6:8]}日で、年齢は{age}歳ですね。")
    if diff_day == 0 :
        print("本日お誕生日、おめでとうございます！")



