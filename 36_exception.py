# 例外処理：例外が発生したらどのような対処をするかを記述しておくこと

# 数あてゲームの例外処理
import random
answer = random.randint(1, 100)
print(answer)

while True:  # 無限ループ
    try: # 例外を発生させる可能性があるコード
        number = int(input('100までの数値を入力してください: '))
    except ValueError: # ValueError例外を処理するコード
        print("数字以外が入力されました。数字のみを入力してください")
        continue

    if answer < number:
        print('もっと小さな数値です')
    elif answer > number:
        print('もっと大きな数値です')
    else:
        break  # 変数answerの値と変数numberの値が等しければ終了

print('素晴らしい！ 正解です！')

# 例外処理その２
while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        selection = int(input('どれにしますか: '))
        if selection == 1:
            tmp = int('foo')  # ValueError <-- 型が異なる
        elif selection == 2:
            tmp = 'str'[5]  # IndexError <-- リストの要素がない
        elif selection == 3:
            print()
            print('例外を発生させませんでした')
        elif selection == 4:
            print()
            print('終了します')
            break
        else:
            print(undefined_var)  # 未定義の変数を参照

        """
        ValueErrorやIndexErrorは、Exceptionクラスを継承している
        そのため、継承構造で上位にある例外クラスは、具体的なクラスよりも下に列挙する必要がある
        """
    #except Exception as e:
    #    print('Exception')
    #    print(e.args)
    #    print()
    
    except ValueError as e:
        print('Value Error')
        print(e.args)
        print()
    except IndexError:
        print('Index Error')
        print()
    except Exception as e:
        print('Exception')
        print(e.args)
        print()
    

    ## 複数の例外を一つのexcept節で補強することも可能　＝タプルを用いて記述
    ## ただし、is-aの関係（継承関係）にない、例外クラス同士のみ

    """
    except (ValueError, IndexError) as e:
        print(e.args)
        print()
    except Exception as e:
        print('Exception')
        print(e.args)
        print()
    except:
        print('Exceptionよりも上位の例外クラスに属する例外が発生しました ')

    """
    print('try文の直後の行を実行しました') # <-- try文の次の文から実行が続く

print('無限ループを終了しました')

## 例外処理その３
while True:
    try:
        print()
        print('1: 例外を発生させる')
        print('2: 例外を発生させない')
        print('3: 終了')
        selection = int(input('どれにしますか: '))
        if selection == 1:
            tmp = 'str'[5]
        elif selection == 2:
            print('例外を発生しませんでした')
        elif selection == 3:
            break
    except IndexError:
        print('IndexError例外が発生しました')
    else:
        print('else節を実行しました')
    finally:
        print('finally節を実行しました')

print()

## 例外処理その４

def raise_exception():
    try:
        raise ValueError()
    except IndexError:
        print('Index Error caught')
    finally:
        print('executing finally clause')

def call_raise_exception():
    try:
        raise_exception()
    except ValueError:
        print('Value Error caught')

def call_raise_exception2():
    raise_exception()

call_raise_exception()
call_raise_exception2()