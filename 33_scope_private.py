#クラスとスコープ、名前空間、プライベートな属性の扱い

##hello,some_methodは、fooクラスの属性となる
class Foo:
    def hello(self):
        print('Hello from Foo')
    def some_method(self):
        local_var = 'local var in hello method'
        print('local namespace:', dir())
        print('global namespace:', globals().keys())
    
##定義終了時に、fooがローカルの名前空間に追加される
##fooが使えるようになる

foo = Foo()
foo.some_method()
print()
## ローカルスコープには、self（パラメータ）とlocal_var（ローカル変数）のみ存在する
## グローバルスコープには、Pythonの実行環境が自動でセットアップするもの＋Foo（クラス）,foo（インスタンス）のみ存在する
"""
クラスで定義した各種メソッドは、インスタンスメソッドから直接【インスタンス変数/メソッド名と引数を指定するだけで】アクセスするわけではない
代わりに、パラメータselfを介してアクセスする。
"""

class Foo:
    def hello(self):
        print('Hello from Foo')
    def some_method(self):
        print('self namespace:', dir(self)) # some_valueがある
        print('Foo namespace:', dir(Foo))   # some_valueがない
        self.hello()

foo = Foo()
foo.some_value = 'some value' # インスタンスで追加する属性
foo.some_method()
print()

# クラスの継承と名前空間とスコープ
class Foo:
    def hello(self):
        print('Hello from Foo')
    def hello_goodbye(self):
        self.hello()
        print('Goodbye from Foo')
    def show_attr(self):
        print(f'{self.__class__}: {dir(self)}')  # __class__:オブジェクトが何の型に属すのかを示す特殊属性

class Bar(Foo):
    def hello(self):
        print('Hello from Bar')
    def goodbye(self):
        print('Googbye from Bar')
"""
２つのクラスと固有の名前空間が作成される。
　Fooには、hello, hello_goodbyeが、objectクラスから受け継いだもの
　Barには、hello,Fooクラスから受け継いだもの、objectクラスから受け継いだもの
が属性として登録される。
"""

foo = Foo()
foo.show_attr()
bar = Bar()
bar.show_attr()
print()
## オーバーライドされており、別々のインスタンスメソッドである　＝　出力結果は異なる
foo.hello()
bar.hello()
print()
## オーバーライドされていない場合は、Fooクラスで定義したものが呼び出される
foo.hello_goodbye()
bar.hello_goodbye()

# プライベートな属性
## プライベート：内部で使うだけ、外部へ見せない　という意味
"""
ケース：
　・モジュール/パッケージの内部だけで使う場合：from モジュール名 import * <-- 23,24章を参照
　・メソッドが長くなるため、いくつかのメソッドに分割する場合
　・クラス内でのみ保存し、外部から自由に触れないメソッドにする場合
"""


class Foo:
    def __init__(self, name):
        self._name = name  # _nameはプライベート
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name
    def show_attr(self):
        print(dir(self))

foo = Foo('deep insider')
print(foo.get_name())  # Fooクラスが用意したメソッドを使ってデータを取得
foo.set_name('atmarkit')  # Fooクラスが用意したメソッドを使ってデータを書き換え
print(foo._name)  # だが、このようにして直接アクセスもできてしまう
"""_メソッド名によるプライベート化は、暗黙の了解でしかない（強制力はない）"""
foo.show_attr() # _nameも表示されてしまう
print()

"""強制力を高めるためには、アンダースコア_を2つにすればよい"""

class Foo:
    def __init__(self, name):
        self.__name = name  # __nameはプライベート
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def show_attr(self):
        print(dir(self))

foo = Foo('deep insider')
print(foo.get_name())  # Fooクラスが用意したメソッドを使ってデータを取得
foo.set_name('atmarkit')  # Fooクラスが用意したメソッドを使ってデータを書き換え
#print(foo.__name)  # エラーとなる
"""
外部からは、_クラス名__インスタンス変数名という名前で見えるようになっている
i.e. 属性の名前を変更している（名前マングリング）
特殊メソッドは、名前マングリングの対象ではない
"""
foo.show_attr() ## _foo.__nameというメソッドがあることを確認する
print()

# プロパティ
"""
プロパティとは、
foo = Foo()
foo._some_value = ……
print(foo._some_value)
のような書き方を許し、プライベートな属性のアクセスする仕組み
"""

## プロパティの名前をmynumとする
## getter,setterをget_num,set_numとし、これらのメソッドの中で__mynum（プライベート）を操作するようにしている

class Foo:
    def __init__(self):
        self.__mynum = 0
    def get_num(self):
        return self.__mynum
    def set_num(self, new_value):
        if 0 < new_value < 101:
            self.__mynum = new_value
        else:
            raise ValueError('value out of range(0-100)')
    mynum = property(get_num, set_num)

foo = Foo()
foo.mynum = 50  # mynumをインタフェースとして__mynumの値を変更
print(foo.mynum)  # mynumをインタフェースとして__mynumの値を取得
# foo.mynum = 101  # 範囲外なのでエラーとなる