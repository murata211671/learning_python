# タプルは[]の代わりに()を用いて定義される

numtuple = (1,2,3)
print(numtuple)

# 要素を変更できないことがリストとの違い
# 変更できないことをimmutable、変更できることをmutableと呼ぶ

# タプルは()を省略して定義できる
# 空のタプルは例外
# ()があっても、要素が一つの場合は、tupleという判定にはならない カンマを置くことでタプルになる

tuple1 = "murata" , "yuki"
print(f"tuple1: {tuple1} , type : {type(tuple1)}")
tuple2 = ()
print(f"tuple2: {tuple2} , type : {type(tuple2)}")
tuple_question = ("Python",)
print(f"tuple_question: {tuple_question} , type : {type(tuple_question)}")

# tuple関数
list = [1,2,3,4]
print(type(list))
tuple = tuple(list)
print(type(tuple))

# タプルは要素の変更ができない
print(f"tuple[0] : {tuple[0]}")
# tuple[0] = 0 # TypeError: 'tuple' object does not support item assignment

# タプルのパック、アンパック
# アンパックは、タプルの要素数と変数の数が一致している必要がある

mytuple = 1,2,3,4 # タプルの生成（パック）
w,x,y,z = mytuple # タプルのアンパック
print(w,x,y,z)

# リストや文字列もアンパック可能である(これらのオブジェクトをPythonではシーケンスアンパックと呼ぶ)
a,b,c = ["murata", "20000201", "24"]
print(f"a: {a} , b: {b} , c: {c}")
x,y,z = "AGE"
print(f"x: {x} , y: {y} , z: {z}")

# タプルの要素変更はできない
# ある変数に、タプルを代入することはできる（タプルの要素変更に見える）

mytuple = 1,2,3
mytuple = 4,5,6
print(mytuple)

# タプルの要素がリストである場合、タプルの要素の要素は変更できる
mylist1 = [1,2,3]
mylist2 = [4,5,6]
mytuple = mylist1,mylist2

print(mytuple)

mytuple[0][0] = -1
print(mytuple)

# リストとタプルの目的
# リスト：同種のデータを複数個並べて管理する　　タプル：異なる（同じ）種類で、関連性のあるデータをひとまとめにする