# import mypkg エラーが表示される　AttributeError: module 'mypkg' has no attribute 'mymath'

## 解決策1: import パッケージ名.モジュール名 で実行する
"""
関数で呼び出すたびに、すべての名前をフルパスで記述する必要がある
"""
# import mypkg.mymath
# print(mypkg.mymath.fact(5))

## 解決策2: from import文を活用する

"""
from mypkg import mymath  # mypkgパッケージのmymathモジュールをインポート
from mypkg.mymath import fact  # mypkg.mymathモジュールからfact関数をインポート

print(fact(5))
print(mymath.fizzbuzz(15))
"""

print(dir())
from mypkg import * # 何もインポートされていない　-> _init_.pyへの記述が必要
print(dir())

# 相対インポート(__init.py__で説明する)
## print(__name__)により、__name__変数の値が表示される


