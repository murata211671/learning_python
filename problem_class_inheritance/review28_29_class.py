from math import sqrt

class Point:
    def __init__(self, x = 0.0, y = 0.0) :  # インスタンスが生成される際に、固有の初期化処理を行う（コンストラクタ）
        self.x = x                          # selfは、初期化対象となるインスタンスのこと（自動的にインスタンス名が代入される）
        self.y = y
    def difference(self, point= None):
        if not point:
            point = Point()  # 原点を表すPointクラスのインスタンス生成
        return sqrt((self.x - point.x) **2 + (self.y - point.y) **2) 


point1 = Point()
print(type(point1))  # __main__ ＝　対話環境
print(dir(object))
print(dir(point1))   # dir は、属性を調べる関数
print()
# インスタンスが持つ個々の値を利用して、計算処理を行うため、インスタンスメソッド
# クラスが持つ属性のことをメンバ


# メンバ（インスタンス変数、インスタンスメソッド）
point1.x = 1.0
point1.y = 1.0
print(dir(point1)) # x,yという属性（インスタンス変数）が増えている

point1 = Point(1.0,1.0)
point2 = Point()

print(f'point1: ({point1.x, point1.y})') # デフォルト値が1.0に変わったあとのものへ初期化される
print(f'point2: ({point2.x, point2.y})')

print()
print("mathのsqrt関数を利用します")
print(sqrt((point1.x - point2.x) **2 + (point1.y - point2.y) **2))

print()
print("2点間の距離を求めます（differnce関数を使う")
print(point1.difference(point2))
point3 = Point(5,4)
print(point3.difference(point1))

# メンバ（クラス変数、クラスメソッド、スタティックメソッド）

# インスタンスごとに固有のデータ（インスタンス変数）は、宣言なしに必要なタイミングで付加できる
point1.hello = lambda x: print("Hello" , str(x))
point1.hello("yuuki")
# point2.hello("yuuki") # Pointクラスの定義にはhelloメソッドがないため、エラー

# クラス変数
import datetime

class MyClass:
    count = 0 # クラス変数countの定義class MyClass:
    today = datetime.datetime.today().date()



# クラス変数へのアクセス　　クラス.クラス変数でアクセスできる
print(MyClass.count)
print(MyClass.today)

instance = MyClass()
print(instance.count)   # インスタンス.クラス変数　でもアクセスできる

print()
instance.count = 100    # インスタンスに同じ名前の変数を定義すると
print(MyClass.count)
print(instance.count)   # インスタンス.クラス変数ではなく、インスタンス.インスタンス変数　を参照することになる
#       ※クラスが持つ属性と同じ名前の属性を、インスタンスに持たせないようにすることも重要


class MyClass:
    count = 0 # クラス変数countの定義
    today = datetime.datetime.today().date()

    def __init__(self):
        self.count += 1         # インスタンス.クラス変数の値を変更　ーー＞　countというインスタンス変数を生成している
        print(f'you made {MyClass.count} instance(s)')

instance = MyClass()            # インスタンス変数を参照してしまっている
instance = MyClass()
print()

class MyClass:
    count = 0 # クラス変数countの定義
    today = datetime.datetime.today().date()

    def __init__(self):
        MyClass.count += 1         # クラス.クラス変数の値を変更する
        print(f'you made {MyClass.count} instance(s)')

instance1 = MyClass()
instance2 = MyClass()
print()

# クラスメソッド
# クラス.クラスメソッド　のようにして呼び出す　　＝インスタンスなしで呼び出せる
class MyClass:
    count = 0
    today = datetime.datetime.today().date()

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod # クラスメソッドの定義
    def get_count(cls):             # クラスメソッドの場合、selfではなくclsを使う
        print(cls.count)

MyClass.get_count()
instance1 = MyClass()
instance2 = MyClass()
instance2.get_count()
print()

# スタティックメソッド  :クラスともインスタンスとも関連付けられていないメソッド
# clsもselfも引数に持たない = クラスやインスタンスが渡されることはない

class MyClass:
    count = 0
    today = datetime.datetime.today().date()

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod # クラスメソッドの定義
    def get_count(cls):             # クラスメソッドの場合、selfではなくclsを使う
        print(cls.count)

    @staticmethod # スタティックメソッドの定義
    def static_get_count():
        print('count:', MyClass.count)
    
MyClass.static_get_count()
instance = MyClass()
instance.static_get_count()

