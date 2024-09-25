"""
代入【=】、累算代入演算子【+= , /=, &= etc】、算術演算子【+ , - ,* , /, // ,%, **】
比較演算子【==, is, is not, in, in not etc】、ブール演算子【or, and, not】、
ビット演算子【&, ^ , |, ~】、シフト演算子【<<, >>】、三項演算子【x if 条件 else y】、代入式【:=】
"""
# 代入
c, d, *e, f = [3,4,5] # *fとすることで、可変長位置引数と同じ役割とみなせる
print(c,d,e,f)

#累算代入演算子 -> アイデンティティを変えずに代入される
mylist = [1,2]
print("mylist id:" , id(mylist))
mylist+= [1,2]
print("mylist id:" , id(mylist)) # アイデンティティの変化がない
mylist = mylist + [3,4]
print("mylist id:" , id(mylist)) # アイデンティティが変化している
print()

# 比較演算子
"""
==, !=, >, >=, <, <= はオブジェクトの値が等しいが否かを判断する
is, is not はオブジェクトのアイデンティティが等しいがどうかを判断する
"""
## 大小関係について
"""
型が異なるー＞等しくない
同じ型、要素数、要素（インデックス、キー）であるー＞等しい
リストなど：対応する要素が異なるー＞小さい値を持つオブジェクト＝小さい
リストなど；要素の値はすべて等しい、他にも要素を持っている場合ー＞要素が少ないオブジェクト＝小さい
文字列：Unicodeを基準とした、辞書式順序で比較
集合：包含関係で大小を決める
"""
mystr1 = 'abc'
mystr2 = 'abcd'
# 'abc'までは同じだが、mystr2には'd'もあるので、mystr2の方が大きい
print(mystr1 < mystr2)  # True

mylist1 = [1, 2, 3]
mylist2 = [1, 2, 4]
# インデックス2で、mylist2の要素の値の方が大きい
print(mylist1 < mylist2)  # True

mytuple1 = ('foo', 'baar', 'baz')
mytuple2 = ('foo', 'bar', 'baz')
# インデックス1で、'baar'と'bar'では'baar' < 'bar'となる（辞書式順序）
print(mytuple1 > mytuple2)  # False

mydict1 = {'foo': 0, 'bar': 1}
mydict2 = {'bar': 1, 'foo': 0}
# 全てのキーと値が等しいので、別オブジェクトだが等価
print(mydict1 == mydict2)  # True

myset1 = {1, 2, 3}
myset2 = {4, 5, 6}
# 集合の包含関係を満たさないので、大小比較はどちらもFalseとなる
print(myset1 > myset2)
print(myset2 > myset1)
print()

# ブール演算子
## 0や0.0 、空の文字列、リスト[]はすべてFalseとみなされる
print(not 1)

if not []:
    print("emplist")
else:
    print("not empty")
print()

## 短絡評価：初めの条件で判定できる場合には、後ろの判定を行わないこと
## and, orは短絡評価である -> 条件1 and 条件2 : 条件1がFalseなら条件2を判定せずにFalse、条件1 or 条件2 : 条件1がTrueなら条件2を判定せずにTrue

# ビット演算子 / シフト演算子
## &: ビット演算子における論理積、|:ビット演算子における論旨和
## ^: 排他的論理和、~: ビット反転
## <<: 左シフト= 0000 0010 -> 0000 1000、>>: 右シフト= 0010 0000 -> 0000 1000とする

x = 39   # 2進数で00100111
y = 142  # 2進数で10001110

print(x & y)  # 6
print(x | y)  # 175
print(x ^ y)  # 169
print(x << 2)  # 156
print(y >> 1)  # 71
print()

# 三項演算子
from random import randint

number = randint(1, 10)
message = 'even' if number % 2 == 0 else 'odd'
print(f'{number} is {message} number')

number = randint(1, 30)
message = 'fizzbuzz' if number % 3 == 0 and number % 5 == 0 \
          else 'fizz' if number % 3 == 0 \
          else 'buzz' if number % 5 == 0 \
          else str(number)
print(f'{number}: {message}')
print()

# セイウチ演算子
## 代入を使わない場合ー＞len関数を二回使われている
s = 'foo'

if len(s) > 5:
    print(f'length of {s}: {len(s)} ( > 5)')
else:
    print(f'length of {s}: {len(s)} ( <= 5)')

## 代入を使う場合
s = 'foo'
n = len(s)

if n > 5:
    print(f'length of {s}: {n} ( > 5)')
else:
    print(f'length of {s}: {n} ( <= 5)')

## :=を使う場合ー＞式の中で代入できる
s = 'foo'

if (n := len(s)) > 5: # := は演算の中で優先度が低い -> ()を加えて優先度を上げる必要がある
    print(f'length of {s}: {n} ( > 5)')
else:
    print(f'length of {s}: {n} ( <= 5)')

## 関数の複数呼び出しを防ぐこともできる
numbers = [0, 1, 2, 3, 4]
def somefunc(x):
    return x * 2
l = [(x, somefunc(x)) for x in numbers if somefunc(x) > 5]
print(l)  # [(3, 6), (4, 8)]

numbers = [0, 1, 2, 3, 4]
def somefunc(x):
    return x * 2
l = [(x, y) for x in numbers if (y := somefunc(x)) > 5] # if句を先に参照されるため、代入のタイミングはif句の中にしている
print(l)  # [(3, 6), (4, 8)]

# 代入式を記述できないケース
## y := 1 はSyntaxErrorとなる
(y := 1) # ()で囲めばOK
