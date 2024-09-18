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
# 相対パス
# モジュールやパッケージの名前に対して、相対的にモジュールを指定すること
# __name__変数により、調べられる
print(__name__)
from mypkg.mymath import fact, fizzbuzz, fib
from mypkg.greet import hello



__all__ = ['fact', 'fizzbuzz', 'fib', 'hello']


