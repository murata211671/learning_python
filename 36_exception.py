# 例外処理：例外が発生したらどのような対処をするかを記述しておくこと

# 数あてゲームの例
import random
answer = random.randint(1, 100)

while True:  # 無限ループ
    number = int(input('100までの数値を入力してください: '))
    if answer < number:
        print('もっと小さな数値です')
    elif answer > number:
        print('もっと大きな数値です')
    else:
        break  # 変数answerの値と変数numberの値が等しければ終了

print('素晴らしい！ 正解です！')

