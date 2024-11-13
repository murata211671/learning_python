# 二つの数値を入力して、その和差積商を求めるコード

## クラス作成をしない場合
"""
print("こちらは、四則演算計算ツールです。")
judge = True
while judge:

    try :
        num1 = int(input("数値1を入力してください->"))
        num2 = int(input("数値2を入力してください->"))

        print("計算結果")
        print(f"num1 + num2 :{num1 + num2}")
        print(f"num1 - num2 :{num1 - num2}")
        print(f"num1 * num2 :{num1 * num2}")
        print(f"num1 // num2 :{num1 // num2}")

    except ValueError:
        print("数値以外が入力されました。数値のみを入力してください")  
    except ZeroDivisionError:
        print("0で割ることはできません")
        print("num2には0以外を入力してください")

    finally :
        if input("引き続き計算を行いますか？ -> No: 0: ") == "0" :
            judge = False
    

print("計算を終了します。またのご利用をお待ちしております。")

"""

## クラスと例外クラスを使用する場合

# class 0：例外クラス
class SomeException(Exception):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__("数値ではありません")
        else:
            super().__init__(args)
            

# class 1：mixin　数字のリストなら合計を、文字のリストなら文字列を、出力する
class Calc() :
    def sum(self) :
        sum = 0
        for item in self.list1:
            sum += item
        print(f"sum: {sum}")
    
    def string(self) :
        string = "" 
        for item in self.list2 :
            string += item + " "

        print(f"string: {string}")

# class 2：数字のリストを作成する
class Numlist(list,Calc) :
    def __init__(self) :
        self.list1 = []

    def addnum(self):
        judge = True
        while judge :
            num = input("数値を入力してください-> ")
            if not num.isnumeric() :
                raise SomeException
            else :
                num = int(num)

            self.list1.append(num)
            print(f"現在のlist1: {self.list1}")

            if input("引き続き計算を行いますか？ -> No: 0: ") == "0" :
                judge = False
        
        print(vars(self))

# class 3：文字のリストを作成する
class Wordlist(list,Calc):
    def __init__(self) :
        self.list2 = []

    def addword(self):
        judge = True
        while judge :
            word = input("文字を入力してください-> ")
            self.list2.append(word)
            print(f"現在のlist2: {self.list2}")

            if input("引き続き計算を行いますか？ -> No: 0: ") == "0" :
                judge = False
        
        print(vars(self))
    

        

num1 = Numlist()
num1.addnum()
num1.sum()

str1 = Wordlist()
str1.addword()
str1.string()




