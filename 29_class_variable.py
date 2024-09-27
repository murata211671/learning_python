# クラスの属性
## 前回で、インスタンス変数、メソッドについて学んだ
## 今回は、クラス変数、クラスメソッド、スタティックメソッドを学ぶ

## クラス変数：クラスに結びつけられた変数
## クラスメソッド：クラスに結びつけられた関数（メソッド）
## スタティックメソッド：クラスを名前空間として、その中に定義された関数（メソッド）

"""
インスタンス変数＝インスタンス固有のデータを保存するもの
クラス変数＝クラス（クラスオブジェクト）に固有データを保存するためのもの
            複数のインスタンスで共有したいデータを保存するために使える
"""
# クラス変数の定義
## クラスの定義の中でそのまま定義する

class MyClass :
    count = 0 # クラス変数countの定義
    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

print(MyClass.count) # クラス.クラス変数とすれば、アクセスできる

instance = MyClass()
print(instance.count) # インスタンスを生成してからアクセスもできる

instance.count = 120
print(f"MyClass.count: {MyClass.count}")
print(f"instance.count: {instance.count}") # インスタンス変数が存在する場合は、クラス変数よりインスタンス変数が優先される

instance1 = MyClass()
instance2 = MyClass()
print()

# クラスメソッド
## 定義の方法１：デコレーター（関数・クラスの定義の前に置き、性能をカスタマイズする）ー@classmethod
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod  # クラスメソッドの定義
    def get_count(cls):
        print(cls.count)  # クラス変数には「cls.クラス変数」としてアクセス

MyClass.get_count()
instance1 = MyClass()
instance2 = MyClass()
instance2.get_count()

## 定義の方法2：classmethod関数を用いる
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod  # クラスメソッドの定義
    def get_count(cls):
        cls.another_get_count()

    another_get_count = classmethod(lambda cls: print('count:', cls.count))

MyClass.another_get_count()
instance1 = MyClass()
instance1.another_get_count()
instance1.get_count()
print()

##クラスメソッドの使い方
## クラスメソッド内で処理を行ったうえで、そのクラスのインスタンスを作成する　<- このメソッドをファクトリメソッドと呼ぶ
## 例：detetimeモジュールのdateクラスのtodayメソッド

# スタティックメソッド
## デコレーター@staticmethod　または　staticmethod関数を使用して定義すｒ
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod  # クラスメソッドの定義
    def get_count(cls):
        cls.another_get_count()

    another_get_count = classmethod(lambda cls: print('count:', cls.count))

    @staticmethod # スタティックメソッドの定義
    def static_get_count():
        print('count:', MyClass.count)
## クラス変数を用いる場合には、「クラス.クラス変数」とする必要がある
MyClass.static_get_count()
instance = MyClass()
instance.static_get_count()