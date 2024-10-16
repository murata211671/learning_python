## 複数のレコードを保持するクラスを作成する

## レコード一つを作成し、複数のクラスで保存する場合

class CalcCost() :
    def cost(self):
        cost_pen = 20 * self.pen
        cost_erazer = 50 * self.erazer
        cost_ruler = 100 * self.ruler
        return print(f"{self.name} さんの金額は、pen: {cost_pen}, erazer: {cost_erazer}, ruler: {cost_ruler} です")
    def cost_All(self):
        summary = 20 * self.pen + 50 * self.erazer + 100 * self.ruler
        return print(f"{self.name}さんの代金は{summary}円です")

class UserBuy(CalcCost) :
    count = 0
    def __init__(self, name, pen, erazer, ruler):
        self.name = name
        self.pen = pen
        self.erazer = erazer
        self.ruler = ruler

        UserBuy.count += 1
        print(f"now {UserBuy.count} th instance are created! ")
    def get(self):
        print(f"name: {self.name}, pen: {self.pen}, erazer: {self.erazer}, ruler: {self.ruler}")
    


class UserShopping(UserBuy, list):
    def __init__(self):
        self.list = []


users = UserShopping()

judge = True
while judge:
    name = str(input("名前を入力してください:"))
    pen = int(input("購入したペンの個数を入力してください:"))
    erazer = int(input("購入した消しゴムの数を入力してください:"))
    ruler = int(input("購入した定規の数を入力してください:"))
    user = UserBuy(name, pen, erazer, ruler)
    users.list.append(user)

    print()
    if int(input("入力を続けますか Yes:1, No:0 ->")) == 0:
        judge = False

print(users.list)
for item in users.list:
    item.get()
    item.cost()
    item.cost_All()


