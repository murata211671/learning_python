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

class Numlist(list) :
    def __init__(self) :
        self.list = []

    def addnum(self):
        judge = True
        while judge :
            num = int(input("数値を入力してください-> "))
            self.list.append(num)
            print(f"現在のlist: {self.list}")

            if input("引き続き計算を行いますか？ -> No: 0: ") == "0" :
                judge = False
        
        print(vars(self))

class Calc(Numlist) :
    def sum(self) :
        sum = 0
        for item in self.list:
            sum += item
        print(f"sum: {sum}")

num1 = Calc()
num1.addnum()
num1.sum() 
