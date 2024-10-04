# 多重継承：複数のクラスからその機能を継承すること
## 多重継承：class A + class B -> class C　, 単一継承の連鎖：class A -> class B -> class C

class A:
    def hello(self):
        print('Hello from A')

class B(A):
    pass

class C(A):
    def hello(self):
        print('Hello from C')

class D(B, C): # 多重継承の部分
    pass
"""
Dクラスのインスタンスに対して、helloメソッドはAとCのどちらが呼び出される？
D -> B -> A (省略： -,-> C -> A) という経路 or D ->B -,-> C (省略: -> A)という経路
    -> B 
D          -> A -> Object というダイヤモンド型の継承構造をしている
    -> C 
　ダイヤモンド型継承問題: Aクラスがメソッドの解決時に、複数登場する事態

メソッドの解決： どのメソッドが呼び出されるかを特定すること
MRO（Method Resolution Order）: メソッドを解決していく順序
"""

d = D()
d.hello() ## class Cのメソッドが呼び出される
print(D. __mro__)

"Pythonでは、C3線形化というアルゴリズムでメソッドを呼び出している"

class A:
    def hello(self):
        print('Hello from A')

class B(A):
    pass

class C: # class Aを継承していない
    def hello(self):
        print('Hello from C')

class D(B, C):
    pass
"""
継承構造
    -> B -> A -> Object 
D
    -> C -> Object
"""
d = D()
d.hello() # class Aのメソッドが呼び出される
print(D. __mro__)
"""
D -> B -> A -> C の順番で検索され、class Aのメソッドが先に見つかる

C3線形化は、幅優先（直接の基底クラスを優先）でも、深さ優先（最初に継承したクラスを優先）でもない
"""
## D(C,B)として、Class Dの継承の順番をC , B という順番にする
class A:
    def hello(self):
        print('Hello from A')

class B(A):
    pass

class C:
    def hello(self):
        print('Hello from C')

class D(C, B):
    pass

d = D()
d.hello() # class Cのメソッドが呼び出される

## 特殊属性__mro__: メソッドを解決する際に、基底クラスをたどっていく順序がわかるようになる
print(D. __mro__)
print()

class B:
    def __init__(self):
        self.b_value = 'B'
        print('class B init')

class C:
    def __init__(self):
        self.c_value = 'C'
        print('class C init')

class D(C, B):
    pass

d = D()
print(D.__mro__) # class Cのインスタンスは生成される、class Bのインスタンスは生成されていない
# print(d.b.value) # 確認-> エラー
"""
supur()関数を用いて、すべての__init__メソッドを呼び出す必要がある
"""


