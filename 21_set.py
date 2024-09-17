# 集合
# 辞書と同様に{}で囲んで表す
set1 = {'Python', 'Java', 'PHP'}
print(set1) 

# 要素が重複しないようになっている
# 集合は、順序を持たない（シーケンスがない）ものである
mylanguages = {'Python', 'Ruby', 'PHP', 'Python'}
print(mylanguages)

# set関数による、集合の定義
# 空集合を定義するためにも用いられる

emptyset = {}  # 実は空の辞書の作成
print( f"emptyset : {emptyset}",type(emptyset))
emptyset = set()  # 空の集合の作成
print(emptyset)
print(f"emptyset : {emptyset}" , type(emptyset))
print()

# リスト・辞書から集合を作成
## リストから出力する
mylist = [1, 2, 3] * 2  # [1, 2, 3, 1, 2, 3]
myset = set(mylist)
print(myset)
## キーが出力する
mydict = {'foo': 'FOO', 'bar': 'BAR'}
myset = set(mydict)  # mydictのキーを要素とする集合
print(myset)
## キーと値を出力する
myset = set(mydict.items())  # mydictの(キー, 値)のタプルを要素とする集合
print(myset)
print()

# 集合の内包表記
myset = {x for x in range(10)}  # 0～9の整数値を要素とする集合
print(myset)

myset = {x for x in range(10) if x % 2 == 0}  # 0～8の範囲に含まれる偶数値
print(myset)