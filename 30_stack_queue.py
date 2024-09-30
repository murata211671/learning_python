# スタックの定義を行う
## スタックの入れ子として、リストを用いる
## スタックは、後入れ先出しであるため、リストの後ろから追加と削除を行うメソッドが必要

class MyStack :
    def __init__(self, *args): ## 可変長位置引数により、複数の要素を引数に持たせる
        self.stack = [] ## 空のリストをスタックに保存する入れ物として定義
        self.stack.extend(args) ## extendメソッドによる追加により、引数から初期化を行う

        """
        for item in args: ## for文により、引数から初期化を行う
            self.stack.append(item)
        """
    
    # 要素を追加するメソッド（後ろへ）
    def push(self, item):
        self.stack.append(item)

    # 要素を削除するメソッド（後ろから）
    def pop(self):
        """
        result = self.stack[-1]
        del self.stack[-1]
        return result
        """
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    # 要素が表示されるメソッド
    def __repr__(self):
        return 'Mystack(' + repr(self.stack)+ ')'
    def __str__(self):
        return str(self.stack)

    # 反復可能オブジェクトとして扱えるようにするメソッド
    def __iter__(self):
        return iter(self.stack)

    # インデックス指定をできるようにするメソッド
    def __getitem__(self, key):
        return self.stack[key]    

## スタックの動作テスト
mystack = MyStack(11,12,13)
mystack.push(0)
mystack.push(2)
mystack.push(1)
mystack.push(1)

print(mystack.stack)
print(f"mystack.pop(): {mystack.pop()}, ", f"mystack.stack : {mystack.stack}")
print(f"mystack.pop(): {mystack.pop()}, ", f"mystack.stack : {mystack.stack}")
print(f"mystack.pop(): {mystack.pop()}, ", f"mystack.stack : {mystack.stack}")
print(f"mystack.pop(): {mystack.pop()}, ", f"mystack.stack : {mystack.stack}")
print(f"mystack.pop(): {mystack.pop()}, ", f"mystack.stack : {mystack.stack}")
print(f"mystack.pop(): {mystack.pop()}, ", f"mystack.stack : {mystack.stack}")



# キューの定義を行う
## キューの入れ子をリストとする
## キューは先入れ先出しであるため、リストの後ろから追加するエンキュー、前から呼び出すデキューのメソッドが必要

## キューの定義
class MyQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        result = self.queue[0]
        del self.queue[0]
        return result

## キューの動作テスト
myqueue = MyQueue()
myqueue.enqueue(0)
myqueue.enqueue(2)
myqueue.enqueue(1)
myqueue.enqueue(2)
print(myqueue.queue)
print(f"myqueue.dequeue(): {myqueue.dequeue()}, ", f"myqueue.queue : {myqueue.queue}")
print(f"myqueue.dequeue(): {myqueue.dequeue()}, ", f"myqueue.queue : {myqueue.queue}")
print(f"myqueue.dequeue(): {myqueue.dequeue()}, ", f"myqueue.queue : {myqueue.queue}")
print(f"myqueue.dequeue(): {myqueue.dequeue()}, ", f"myqueue.queue : {myqueue.queue}")
print(f"myqueue.dequeue(): {myqueue.dequeue()}, ", f"myqueue.queue : {myqueue.queue}")

# スタック、キューを更に使いやすくするメソッド：特殊メソッド
"""
次のようにして、より使いやすいクラスへと変えていく
　・インスタンスの生成時に、初期値を与える
　・print関数などに、クラスインスタンスを渡したときに、その要素が表示する
　・for文と組み合わせて使用
　・インデックス指定により、特定の要素を取得する
"""

## これらを実現できるようにするメソッド　＝　特殊メソッド
print(f"str(mystack): {str(mystack)}")
print(f"repr(mystack): {repr(mystack)}")

mystack = MyStack(1, 2, [3, 4])
for item in mystack:
    print(item)


print(mystack[0])
print(mystack[0:2])  # スライスできるか？-> 可能である

## これら以外にも、様々な特殊メソッドが存在する。
## コンテナやシーケンスに属するクラスを定義する際には、さらに多くのメソッドや関数類を定義する必要がある。
## 詳しくは、Pythonのドキュメント「コンテナをエミュレートする」を参照