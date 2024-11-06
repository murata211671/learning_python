# 例外の送出　：raise文を用いて発生させること
## 自分で関数・メソッドを定義している際に、パラメータに受け取った値が想定したものとは異なる場合など、それらの関数やメソッドで処理ぞ続行させることが不可能なときに、
## 例外を送出することで、呼び出した側に異常事態の発生を知らせることができる

class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):

        """
        if len(self.stack) == 0: ## スタックに要素がない場合に、Noneを返す
            return None
        """

        if len(self.stack) == 0 :
            raise IndexError('stack is empty') ## IndexError例外を送出して、「スタックが空である」ことを伝える
        return self.stack.pop()

        ##　このようにすると、以下のメッセージが出力される

        """
0
Traceback (most recent call last):
  File "/workspace/37_exception_class.py", line 35, in <module>
    print(mystack.pop())
          ^^^^^^^^^^^^^
  File "/workspace/37_exception_class.py", line 17, in pop
    raise IndexError('stack is empty') ## IndexError例外を送出して、「スタックが空である」ことを伝える
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: stack is empty
        """
        

        

mystack = MyStack()
mystack.push(0)
print(mystack.pop())

# コードや仕様の変更が及ぼす影響
## クラスを利用している部分のコードも、例外の処理の書き方に直す必要である

mystack.push(2)

item = mystack.pop()

## 元々、以下のようになっていたコードを
if item != None :
    print(f"item: {item} ")

### mystack.push(3)

## 次のように変更が必要となる
try:                            ## 例外処理のtry文に直す
    item = mystack.pop()
except IndexError as e:         ## 例外をキャッチした場合の処理
    print(e)  # 例外を処理
else:                           ## 正常に動いた場合の処理
    print(f"item: {item}")  

"""
他の人にも使ってもらうコードを書いている場合には、コードの振る舞いをどのようにするべきかを慎重に検討する必要がある
"""
print()

# 例外クラス
## 例外クラスの定義を行う際の、注意点
## Exceptionクラス（その派生クラス）を継承するクラスとする

## 
class EmptyStackError(Exception):
    def __init__(self, *args):
        if len(args) == 0:  # 引数が渡されなかったら基底クラスの__init__
            super().__init__('stack is empty')  # メソッドにメッセージを渡す
        else:  # 引数が渡されたら全てを基底クラスの__init__メソッドに渡す
            super().__init__(args)

class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            raise EmptyStackError
        return self.stack.pop()

mystack = MyStack()
mystack.push(0)
print(mystack.pop())
print(mystack.pop())
