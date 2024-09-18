# モジュールのインポートを行う
## 用いる関数を指定しない場合
import random
## モジュールの名前を別名で使いたい場合
import module as mod

## 特定の関数だけをインポートする場合
from module import info

num = 0
numset = set()

while num < 15 :
    num = random.randint(1,20)
    print(num)
    numset.add(num)

print(numset)
# mod.hello()
info()
