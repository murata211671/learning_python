# 辞書（連想配列）；キーと値の組で表されるデータ を複数格納できるデータのこと

# 辞書の定義
# {キー1 : 値1 , キー3 : 値2 } のように定義する
# キーは一つしか定義できない

indi_dict = {"id" : 1 , "name": "Murata" , "birthday": "20000201" , "age" : 24
            , "id" : 101}
            
print(indi_dict)

# 空の辞書の作成：{}のみ
mydict = {}
print(mydict)

mydict = dict()
mydict = dict(name="Murata", age=24) # キーワード引数による辞書作成
print(mydict)
mydict = dict({'foo': 'FOO', 'bar': 'BAR'})  # 辞書を基にした辞書作成
print(mydict)
mydict = dict([('foo', 1), ['bar', 2]])  # 反復可能オブジェクトを使った辞書作成
print(mydict)
mydict = dict({'foo': 'FOO', 'bar': 'BAR'}, baz='baz')  # 組み合わせ
print(mydict)



# 内包表記
names = ["yuki", "mizuki", "noriko"]
ages = [24, 18, 53]
birthdays = ["20000201", "20061019", "19720430"]

# 辞書の内包表記
family_mem = { n : { "age" : a , "birthday" : b } for n,a,b in zip(names, ages, birthdays)}
print(family_mem)

for key, list in family_mem.items() :
    print(key, "さんの誕生日は", list["birthday"] ,"で、年齢は", list["age"], "です")

# 辞書から要素を取り出す方法
"""
 1 : 角かっこ[]にキーを指定する
 2 : getメソッドを使用する
 3 : popメソッドを使用する
 4 : popitemメソッドを使用する
"""
# 1 : 角かっこ[]にキーを指定する

sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
print(sk['first_name'])

#  2 : getメソッドを使用する

sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
print(sk.get('first_name'))  # 存在するキーを指定
print(sk.get('age'))         # 存在しないキーを指定
print(sk.get('age', 'not found'))  # 存在しないキーと、デフォルト値を指定

# 要素の変更と追加
sk["first_name"] = 'Murata'
print(sk)
sk["age"] = 24
print(sk)
# 辞書の結合による追加はできない
# sk = sk + {"birthday" : "20000201"}
print()

# 辞書の操作
# 基本的には、リストと同じである

# 辞書特有の操作
mydict = {'foo': 'FOO', 'bar': 'BAR', 'baz': 'BAZ'}
print(mydict)  # 元の辞書
mydict.update(foo='fooo', somekey='somevalue')  # キーワード引数による辞書の更新
print(mydict)
mydict.update({'bar': 'new BAR'})  # 辞書による辞書の更新
print(mydict)
mydict.update([('baz', 'new Baz'), ['x', 1]])  # リストによる辞書の更新
print(mydict)
mydict.update([('y', 2)], z=3)  # 両者の組み合わせ
print(mydict)
print()

# popメソッドによる値の取得・削除
# キーを受け取って、辞書からは削除する 戻り値はキーに対応した値

mydict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}
print(mydict)
result = mydict.pop('bar')  # キー'bar'に対応する項目を削除
print(result)  # 削除した項目が戻り値になる
result = mydict.pop('bar', 'not found')  # デフォルト値を指定
print(result)  # キー'bar'はないので、デフォルト値が戻り値になっている
print(mydict)

# popitemメソッドによる値の取得・削除
# キーを受け取って、辞書からは削除する　戻り値は、(キー,キーの値)というタプル

mydict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}
print(mydict.popitem())
print(mydict.popitem())
print(mydict.popitem())

# setdefaultメソッド
# 辞書内にキーあればその値を返す　なければキーとその値を格納する
mydict = {'foo': 'foo', 'bar': 'bar'}
print(mydict.setdefault('foo'))  # 存在するキーを指定すれば、その値が返される
print(mydict.setdefault('baz', 'baz'))  # 存在しないキーを指定
print(mydict)

# 辞書項目の反復処理
sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
for item in sk:
    print(item)

# ビューオブジェクトを送信するメソッド
# keys / values / itemsメソッド
# keysメソッド　格納されているキーを一覧するものを返す
# valuesメソッド　格納されている値を一覧するものを返す
# itemsメソッド　格納されているキーと値を一覧するものを返す

sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
for key, value in sk.items():
    print(key, value)

# ビューオブジェクトが動的であることを示す
mydict = {'foo': 'foo'}
myview = mydict.keys()
print(myview)
mydict['bar'] = 'bar'
print(myview)

sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
print('kawasaki' in sk)  # False　辞書にinを用いる場合は、キーの照合をしている
print('kawasaki' in sk.values())  # True　辞書の中の値（のタプル）にinを実行している

# 辞書の活用について
"""
格納されているデータに名前を付けることで扱いを容易にする」あるいは
整数インデックスでは管理が難しいデータを扱う」ためのもの
"""
print()

# キーとしてリスト（ミュータブルなもの）は設定できない
"""
key_list1 = [0, 1, 2, 3]
key_list2 = [0, 1, 2, 1]
print(key_list1 == key_list2)  # False

mydict = {key_list1: 'foo', key_list2: 'bar'}
key_list1[3] = 1
print(key_list1 == key_list2)  # True
"""


# タプルをキーとしても、その要素がリストであるため、キーとして設定できない
"""
key_tuple1 = (1, 2)
key_tuple2 = ([0, 1], [2, 3])  # タプルの要素のリストは変更可能

mydict1 = {key_tuple1: 'foo'}
mydict2 = {key_tuple2: 'bar'}  # エラー
"""

def myfunc(mapping=None, **kwargs):
    if mapping:
        print(mapping)
    for key, value in kwargs.items():
        print(key, value)

mydict = {'foo': 'FOO', 'bar': 'BAR'}
myfunc(11)
myfunc(mydict)  # 辞書をそのまま渡す
myfunc(**mydict)  # 辞書を展開して渡す