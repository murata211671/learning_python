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

