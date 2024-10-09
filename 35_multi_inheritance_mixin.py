# 多重継承とmixin

## インスタンス変数の共有にまつわる問題
class Stack:
    def __init__(self):
        self.x = []
    def push(self, item):
        self.x.append(item)
    def pop(self):
        return self.x.pop()

class Queue:
    def __init__(self):
        self.x = []
    def enqueue(self, item):
        self.x.insert(0, item)
    def dequeue(self):
        return self.x.pop()

mystack = Stack()
mystack.push(1)
mystack.push(2)
print(mystack.x)
print(mystack.pop())
print(mystack.pop())

myqueue = Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
print(myqueue.x)
print(myqueue.dequeue())
print(myqueue.dequeue())
print()

""" ↑ 問題なく動作していることの確認 """

#3 スタックとキューを多重継承したもの
class StackQueue(Stack, Queue):  # スタックであり、キューであるもの
    pass

mysq = StackQueue()
mysq.push(1)
mysq.push(2)
mysq.enqueue(3)
mysq.enqueue(4)
print(mysq.x) # [1,2,3,4]と挿入される（と思われるが実際は違う）
print(mysq.dequeue())  # 最初に入れたデータは「1」が取り出されるか --> No
print(mysq.pop())  # 最後に入れたデータは「4」が取り出されるか  --> No

"""
StackQueueクラスのリスト: [4,3,1,2]
stackのpushメソッドを使って、[] -> [1] -> [1,2]と追加される
queueのenqueueメソッドを使って、[1,2] -> [3,1,2] -> [4,3,1,2]と追加される
"""

"""
問題点：
多重継承によって、扱い方の異なる同名のインスタンス変数を共有してしまった
むやみに多重継承を行うと、複数の基底クラスでインすテンス変数を定義している場合に、多重継承したクラスで問題を引き起こす可能性があ
"""
print(StackQueue.__mro__) # インスタンス変数は、Stackで初期化が行われている -> Stackで初期化したStackQueue.xにenqueueを行っていることになる
print()

"""
または、インスタンス変数を含むクラスを継承するのは、１つだけとするルールを課す場合もある
この場合、追加で継承できるのは、、メソッドのみを含んだクラスとなる
"""

## mixin：幅広いクラスで共通して使われる機能（だけ）を、継承を使って組み込むこと

"""
継承とmixinの使い分け
継承：基底クラスの機能を受け継ぎながら、必要に応じて、その振る舞いを変更、新しい機能を追加して、特殊なクラスへと仕立てる
mixin：すでにある機能を、親子関係にない複数のクラスで共通に利用する
"""

# インスタンス変数を持たず、初期化が必要ないクラス
class Util:
    def show_members(self):
        print(self.__dict__)
    def show_mro(self):
        print(self.__class__.__mro__)


# インスタンス変数を持つ、初期化が必要なクラス
class Foo:
    def __init__(self):
        self.foo = 'FOO'

# Fooクラスを継承し、Utilクラスをmixinしている
class Bar(Foo, Util):
    def __init__(self):
        super().__init__()
        self.bar = 'BAR'

"""
継承階層
Bar --継承--> Foo -- 継承 --> Object
     |
      -- mixin --> Util
"""

bar = Bar()
bar.x = 100
bar.show_members() #３つのインスタンス変数が表示されたことがわかる
print()

##  Utilクラスは、全く異なるクラス階層を構成する場合であっても自由に利用できる
class Base:
    pass

class Derived(Base, Util):
    def __init__(self):
        self.some_value = 100

# mixinされたクラスの挙動を変更する
## テンプレートメソッドパターン：大枠の処理を定義しておき、mixinした側のクラスで、独自の振る舞いを実現する方法

class Util:
    def mixin_method(self): ## antherメソッドを呼び出すのみ
        self.another_method()
    def another_method(self): ## NotImplementError例外を発生させるだけ <-- Utilクラスをmixinした側でオーバーライドする必要があることを伝える
        raise NotImplementedError('method not implemented')

# Utilクラスを複数のクラスへmixinする
class Foo:
    pass

class Bar(Foo, Util):
    def __init__(self):
        self.x = 'BAR'
    def another_method(self):
        print('Hello from', self.x)

class Baz(Foo, Util):
    def __init__(self):
        self.y = 'BAZ'
    def another_method(self):
        print('Hello from', self.y)

class Qux(Foo, Util):
    pass

bar = Bar()
baz = Baz()
qux = Qux()
bar.mixin_method()
baz.mixin_method()
# qux.mixin_method()
print()

"""
mixinクラスは、単体では役に立たない（データのない処理だけであるため）
特に、インスタンスを生成しても意味がない

util = Util()
util.mixin_method() # 例外が発生するだけ
"""

class Util:
    def show_members(self):
        print(self.__dict__)
    def show_mro(self):
        print(self.__class__.__mro__)

util = Util()
util.show_members()
util.show_mro()