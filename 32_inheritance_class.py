# リストを継承して、スタックを定義する

class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    
## 前回まで、アクセスの設定や文字列表現をオーバーライドしていた
class MyStack2:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

        # オーバーライド部分

    def __repr__(self):
        return 'MyStack(' + repr(self.stack) + ')'
    def __str__(self):
        return str(self.stack)
    def __iter__(self):
        return iter(self.stack)
    def __getitem__(self, key):
        return self.stack[key]

## リストクラスを継承して、スタックを実装した場合の振る舞い
class MyStack3(list):
    def push(self, item):
        self.append(item)
"""
クラスの中身は一つの定義で済む
しかし、前々回のスタックと同様の処理が可能である
"""

mystack = MyStack3()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
print(f"type(mystack): {type(mystack)}",mystack)
print(mystack.pop())
print(mystack.pop())
for item in mystack:
    print(item)
print(mystack[1:])
print()

"""
リストクラスを継承する意味：
なぜ、コードの量を減らせるに至ったのか？
"""

## 基底クラスとしてlistを指定 append,popメソッドはそのまま使える
## それぞれのクラスのメソッドを確認する
print('MyStack:', dir(MyStack)) # オブジェクトクラスのメソッドのみ
print('---')
print('MyStack2:', dir(MyStack2)) # オブジェクトクラスのメソッド,　クラスメソッドとして定義したもの
print('---')
print('MyStack3:', dir(MyStack3)) # オブジェクトクラス, リストクラスのメソッド

"""
MyStack3は継承の関係 = is-aの関係 ----スタックはリスト（の一種）
MyStack2は包括の関係 = has-aの関係----スタックはリストを包括する
何のメソッドを使うかによって使い分ける必要がでてくる。
"""


