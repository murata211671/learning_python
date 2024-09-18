# モジュールの使用
import myutil
## fib関数を指定する
from myutil import fib
## fizzbuzz関数を指定する　名前をfbとして使用する
from myutil import fizzbuzz as fb

print(myutil.PI)

numlist = []
for num in range(5):
    print(myutil.fact(num))
    numlist.append(myutil.fact(num))
print(numlist)

for num in range(5):
    print(fib(num))

for num in range(1, 6):
    print(fb(num))


# モジュール名.識別子　の形式で関数にアクセスする場合について
# 識別子のことをモジュールの属性と呼ぶことがある

# 属性の非公開化
## 定義する関数をアンダースコア_で始めると、
##「from モジュール名 import *（すべての関数という意味）」形式でインポートを行う場合に、インポートしない設定にできる。
from myutil import *
print(myfunc1(2))
print(myfunc2(2))
# print(_myhelper(2))

# モジュール検索パス
# 検索パスに含まれるフォルダ
"""
Python処理系を起動したときのカレントフォルダ（あるいは、pythonコマンドに指定したスクリプトファイルがあるフォルダ）
環境変数PYTHONPATHに記述されているフォルダ
インストールされているPythonに固有のフォルダ
"""
