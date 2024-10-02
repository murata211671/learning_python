# クラスの役割
## 関数：何らかの定型処理を行うひとまとまりのコードを再利用するための仕組み
## パッケージ/モジュール:複数の関数などを１つ以上のファイルにまとめることで、それらをほかのコードから再利用するための仕組み
## クラス：何らかのデータ（インスタンス変数）と、処理するためのメソッドをひとまとめにして、名前を付けることで、後からそれらを再利用するための仕組み

"""
継承：何らかのクラスからその属性を受け継ぐこと 
継承元のクラスーー基底クラス、親クラス、スーパークラス
継承先のクラスーー派生クラス、子クラス、サブクラス　　　と呼ぶ
"""

# クラス継承の方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print('Hello,', str(self.name))
    def get_age(self):
        return self.age

kawasaki = Person('kawasaki', 250)
isshiki = Person('isshiki', 19)
kawasaki.hello()
print(isshiki.get_age())

## Studentクラスの定義
class Student(Person):
    pass

kawasaki = Person('kawasaki', 250)
isshiki = Student('isshiki', 18)
print(type(kawasaki))
print(type(isshiki))
isshiki.hello()  # 基底クラスのメソッドを呼び出す
print()

# 派生クラスに属性を追加する（オーバーライド）
class Student(Person):
     ## Student(...)で呼び出した場合、こちらの__init__が呼び出される
     ## Pythonでは、Person()の__init__は呼び出されないことに注意
    def __init__(self, name, age, school): 
        super().__init__(name,age) ## これを付随することで、基底クラスのメソッドにアクセスできるようになる。
        self.name = name
        self.age = age
        self.school = school
    def get_school(self):
        return self.school

isshiki = Student('isshiki', 18, 'Imperial univ')
isshiki.hello()
print(isshiki.get_school())

# クラス/インスタンスが特定のクラスに属するかを調べる
## isinstane(obj, class) :objに受け取ったオブジェクトがclassで指定されるクラスのインスタンスであるときtrue, そうでないときはfalse
## issubinstance(class1, class2): class1に受け取ったクラスが、class2で受け取ったクラスである（派生クラス）であるときtrue, そうでないときはfalse

# 整数値「100」はfloat型のインスタンスか
print('isinstance(100, float):', isinstance(100, float))

# studentはPersonクラスのインスタンスか
student = Student('isshiki', 18, 'Imperial univ')
print('isinstance(student, Person):', isinstance(student, Person))

# StudentクラスはPersonクラスの派生クラスか
print('issubclass(Student, Person):', issubclass(Student, Person))

# PersonクラスはPersonクラスの派生クラスか
print('issubclass(Person, Person):', issubclass(Person, Person))

# 「100」はfloatクラスまたはstrクラスのインスタンスか
print('isinstance(100, (float, str)):', isinstance(100, (float, str)))

# StudentクラスはPersonクラスまたはStudentクラスの派生クラスか
print('issubclass(Student, (Person, Student)):', issubclass(Student, (Person, Student)))

## オブジェクトの型判定には、isinstance()組み込み関数が使われる
