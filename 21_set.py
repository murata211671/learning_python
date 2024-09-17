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
print()

# addメソッド：集合に要素を追加するメソッド
## 集合に集合を要素として追加できない（辞書も同様）
myset = {1, 2, 3}
myset.add(4)  # 要素「4」を集合に追加
print(myset)
#myset.add({5, 6})  # 要素「{5, 6}」を集合に追加
# print(myset)
print()

# remove/discard/popメソッド：集合から要素を削除するメソッド

## discard；集合の要素にあっても、なくても削除する
## remove：集合の要素にあるものたけを削除する
## pop：辞書と同様の操作

myset = {x * 2 for x in range(4)}  # {0, 2, 4, 6}
print(myset)
myset.discard(5)  # エラーにならない
print(myset)
# myset.remove(5)   # エラーになる
print()

# 集合の比較
## 集合の一致
myset1 = {1, 2, 3}
myset2 = {3, 2, 1}
myset3 = {1, 2, 3, 4}

print(myset1 == myset2)
print(myset2 == myset3)
print(myset1 != myset3)

## issubsetメソッド, issupersetメソッド：　部分集合、包含関係
myset1 = set(range(5))  # {0, 1, 2, 3, 4}
myset2 = set(range(4))  # {0, 1, 2, 3}
myset3 = set(range(4))  # {0, 1, 2, 3}
print('myset1', myset1)
print('myset2', myset2)
print('myset3', myset3)

print('myset1.issubset(myset2)', myset1.issubset(myset2))  # False
print('myset2.issubset(myset1)', myset2.issubset(myset1))  # True
print('myset1.issuperset([0, 1, 2])', myset1.issuperset([0, 1, 2]))  # True
print('myset1 <= myset2', myset1 <= myset2)  # False
print('myset2 >= myset1', myset2 >= myset1)  # False
print('myset1 > myset2', myset1 > myset2)   # True
print('myset2 < myset1', myset2 < myset1)   # True
print('myset2 > myset3', myset2 > myset3)   # False
print('myset2 < myset3', myset2 < myset3)   # False
print()

# union/ defference/ intersection/ symmetric_difference メソッド：集合の和・差・積・対称差
## 集合の和：unionメソッド、| 演算
myset1 = {1, 2, 3}
myset2 = {4, 5, 6}
myset3 = {1, 3, 5, 7}

myset4 = myset1.union(myset3)
print(myset4)

myset4 = myset1 | myset2 | myset3
print(myset4)

## 集合の差：differenceメソッド、-演算
myset1 = set(range(7))  # {0, 1, 2, ……, 6}
myset2 = {x for x in range(4, 9, 2)}   # {4, 6, 8}
myset3 = {x for x in range(0, 4, 2)}  # {0, 2}

myset4 = myset1.difference(myset2)
print(myset4)

myset4 = myset1 - myset2 - myset3
print(myset4)

# 集合の席：intersectionメソッド、&演算
myset1 = set(range(1, 6))     # {1, 2, 3, 4, 5}
myset2 = set(range(2, 7, 2))  # {2, 4, 6}
myset3 = {x for x in range(6) if x % 2}  # {1, 3, 5}

myset4 = myset1.intersection(myset2)
print(myset4)

myset4 = myset1 & myset3
print(myset4)

# 集合の対称差：symmetric_differnceメソッド、^演算
## 対称差：集合の和から共通部分を除く
myset1 = set(range(4))      # {0, 1, 2, 3}
myset2 = set(range(2, 6))   # {2, 3, 4, 5}
myset3 = set(range(-2, 2))  # {-2, -1, 0, 1}

myset4 = myset1.symmetric_difference(myset2)
print(myset4)

myset4 = myset1 ^ myset3
print(myset4)
print()

# 集合の更新
## update/ difference_update/ intersection_update/ symmetric_difference_updateメソッド
## 和・差・積・対称差を求めて、集合を更新するもの
myset1 = set(range(0, 10, 2))  # {0, 2, 4, 6, 8}
myset2 = set(range(1, 11, 2))  # {1, 3, 5, 7, 9}
myset3 = set(range(5))         # {0, 1, 2, 3, 4}

myset1.update(myset2)  # myset1とmyset2の和でmyset1を更新
print(myset1)  # {0, 1, 2, ……, 8, 9}

myset1 -= myset2  # myset1とmyset1の差でmyset1を更新
print(myset1)  # {0, 2, 4, 6, 8}

myset1.intersection_update(myset3)  # myset1とmyset3の積でmyset1を更新
print(myset1)  # {0, 2, 4}

myset2 ^= myset3  # myset2とmyset3の対称差でmyset2を更新
print(myset2)  # {0, 2, 4, 5, 7, 9}

myset1 = set()  # 空の集合を作成
myset1 |= {1, 2} | {3, 4} | {5, 6}  # 複数の集合で集合myset1を更新
print(myset1)

print()

# frozenset：一度設定したら、要素の変更（要素の追加、削除、更新）ができない集合
myset = set(range(5))
myfrozenset = frozenset(myset)

print(myfrozenset)
# myfrozenset.add(5)　：frozensetとして定めると、要素の追加ができない
## frozensetは、辞書のキーとして活用できる
