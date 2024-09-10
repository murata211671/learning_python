# リストの繰り返し処理
languages = ['Python', 'Ruby', 'PHP']

print(languages)

counter = 0
for language in languages:
    language = f'{counter}: {language}'
    counter += 1

print(languages)


# リストの要素表示1
print()

for index in range(len(languages)):
    languages[index] = f"{index} : {languages[index]}"

print(languages)
print()

languages = ["Python", "Ruby","PHP", "Java", "Javascript"]


# リストの要素表示２
# enumerate関数
# (リスト, インデックスの初期値)という組としてタプルを要素とするイテレータを返す
print(enumerate(languages))

for (index, language) in enumerate(languages):
    languages[index] = f"{index} : {language}"

print(languages)
print()

# 2つのリストを活用する
# indexを媒介するという手間がある
emplist = ["yuuki", "mizuki", "noriko"]
agelist = [24, 17, 50]

for index, name in enumerate(emplist) :
    print(f"{name}さんの年齢は、{agelist[index]}歳です")
print() 

# zip関数
# 2つ以上のリストの要素をまとめたイテレータを作成する
for name, age in zip(emplist, agelist):
    print(f"{name}さんの年齢は、{age}歳です")
print()

# zip関数で作成されるイテレータは、リストの要素数が少ない方に合わせる
empid = list(range(10))
empname = ["miyakawa", "matsuura", "moriyama", "murata"]

for id, name in zip(empid, empname):
    print(f"id : {id} , name : {name}")
print()

# イテレータ
"""
intlist = [0, 1, 2]
iterator = iter(intlist)

print(iterator.__next__())
print(next(iterator))
print(iterator.__next__())
print(next(iterator))
"""
# イテレータ（次の値が取り出せるもの）は、「要素の反復取り出し」を全要素で一度だけ行う　→　全要素を出した後はエラーがでる
# リスト（反復可能オブジェクト）は、常に任意の要素にアクセス可能である


# map関数
# リストの各要素に対して、一定の処理を加えて得られた結果を要素とするイテレータを返す
# map(function , iterable, ...)

intlist = list(range(9))
result = map(lambda x : x * x ,intlist)

print(intlist)

print("map関数:" , list(result))
print ("内包表記:" , list(x*x for x in intlist))

# filter関数
# 条件を満たすもののみを要素とするイテレータを戻り値とする
intlist = list(range(10))  # [0, 1, 2, ..., 9]
result = filter(lambda x : x % 2 == 0, intlist)  # 偶数だけを選択
print(intlist)
print(list(result))

# all関数、any関数
# all（iterable）:反復可能オブジェクトのすべての要素がTrueの場合にTrueを返す。Falseが一つでもあればFalseを返す。
# any(iterable) : 反復可能オブジェクトのいずれかがTrueなら、Trueを返す。すべてFalseならFalseを返す。

intlist1 = list(range(5))  # [0, 1, 2, 3, 4]
intlist2 = list(range(1, 6))  # [1, 2, 3, 4, 5]
intlist3 = [0] * 5  # [0, 0, 0, 0, 0]
strlist1 = ['', 'foo', 'bar']
strlist2 = ['foo', 'bar', 'baz']
strlist3 = [''] * 5
emptylist = []

# 0以外の数値、空ではないリスト、文字列はTrueとみなす

print('all(intlist1):', all(intlist1))  # False：0は「偽」と見なされる
print('all(intlist2):', all(intlist2))  # True
print('all(intlist3):', all(intlist3))  # False：0は「偽」と見なされる

print('any(strlist1):', any(strlist1))  # True
print('any(strlist2):', any(strlist2))  # True
print('any(strlist3):', any(strlist3))  # False：空文字列は「偽」と見なされる

print('all(emptylist):', all(emptylist))  # True：空のリストを渡すと戻り値はTrue
print('any(emptylist):', any(emptylist))  # False：空のリストを渡すと戻り値はFalse