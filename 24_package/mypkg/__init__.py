# from mypkg import * を使いたい場合
## エラー
"""
import mymath
import greet
"""

## エラー
"""
import mypkg.mymath
import mypkg.greet
"""
# 相対インポート
# モジュールやパッケージの名前に対して、相対的にモジュールを指定すること
# __name__変数により、調べられる
print(__name__) # 変数の値が表示される　　　今回の場合はmypkg

# 絶対インポートを行う場合のインポート文
"""
from mypkg.mymath import fact, fizzbuzz, fib
from mypkg.greet import hello
"""

# 相対インポートを行う場合のインポート文

from .mymath import fact, fizzbuzz, fib
from .greet import hello




__all__ = ['fact', 'fizzbuzz', 'fib', 'hello']


