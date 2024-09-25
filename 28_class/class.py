from math import sqrt

# クラス: Pythonの中でプログラマが独自に作り出した型のこと
print(type("murata")) # strクラスであるという意味
print(type(3.14)) # intクラスであるという意味
## class 型 という形式で表示されることがわかる
print()

"""
オブジェクトとクラスの違い、インスタンス

オブジェクト：コンピュータのメモリ上に存在する何かしらのデータ
クラス：オブジェクトを作成するための設計図
インスタンス：あるクラスかの設計図から作り出され、メモリ上に存在する実態（オブジェクトの言い換え）
"""

# クラスの定義

class Point: # class クラス名:とする　 クラス名は大文字＋CapWord規則に従う
    # pass # 何もしないを意味する文

    def __init__(self, x=0.0, y=0.0): ## 初期化を行うメソッド
        self.x = x # 初期化対称のインスタンスの属性x
        self.y = y # 初期化対称のインスタンスの属性yを意味する

    def difference(self, point=None): # 距離を求めるメソッド
        if not point:
            point = Point()  # 原点を表すPointクラスのインスタンスを生成
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

point1 = Point()
print(type(point1)) # __main__環境上で定義されたクラスであることを意味

# オブジェクトクラス
"""
Pythonのオブジェクトが持つべき基本の属性が自動的に受け渡されている
クラス定義は、実際には class Point(object): を実行していた

実際、()の中身には元となるクラスを列挙していく
特定のクラスを基にして、新しくクラスを作成することを継承と呼ぶ
"""

print(dir(point1))
print()

# クラスとインスタンスの属性
"""
インスタンス変数：クラスの個々のインスタンスが持つ変数
インスタンスメソッド：インスタンスが持つ個々の値を利用して計算処理を行うもの
メンバ：クラスが持つ属性の異なる呼び名
"""

## インスタンス変数の定義
point1.x = 1.0
point1.y = 1.0
print(dir(point1))  # x,yという属性が追加された
point2 = Point() # 異なるインスタンスの定義

# __init__メソッド
## インスタンスが生成される際に、インスタンスごとに固有の初期化処理を行うメソッド 
## =コンストラクタに似た処理を行う

point1 = Point(1.0, 1.0)
point2 = Point()
print(f'point1: ({point1.x}, ({point1.y})')
print(f'point2: ({point2.x}, ({point2.y})')

## 距離を求める操作
print(sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2))
print()

# インスタンスメソッド
point1 = Point(1.0, 1.0)
point2 = Point()
point3 = Point(5, 4)

print(point1.difference(point2))
print(point1.difference())
print(point3.difference(point1))