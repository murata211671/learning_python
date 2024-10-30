## 演習問題

class Member:
    member = ['muto', 'myojin', 'murata', 'mochiduki', 'mori']
    def __init__(self):
        # Member.member.append("murata")
        self.member = []    
    def enter(self, item):
        self.member.append(item)
    def remove(self, item):
        self.member.remove(item)


# myname = input("what your name?: ")

member1 = Member()
member1.enter("muto")
member1.enter("myojin")
member1.enter("murata")
member1.enter("mochiduki")
member1.enter("mori")
print(member1.member)
# member1.remove(myname)
# print(member1.member)

member2 = Member()
member2.enter("furuta")
member2.enter("hotta")
member2.enter("miyahara")
member2.enter("myojin")
member2.enter("murata")
print(member2.member)
# member2.remove(myname)
# print(member2.member)


class Dict(Member):
    def __init__(self):
        self.dict = dict()
        i = 0
        while i < len(self.member):
            self.dict[i] = self.member[i]
            i += 1

MemberWithId = Dict()
print(MemberWithId.dict)

class Personal:
    def __init__(self):
        self.database =[]
        self.data = dict()
    def setData(self, firstname, secondname, age, birthday, firstlanguage):
        self.data["fn"] = firstname
        self.data["sn"] = secondname
        self.data["age"] = age
        self.data["birth"] = birthday
        self.data["fl"] = firstlanguage
        self.database.append(self.data)

personal1 = Personal()
print(personal1.database)
personal1.setData("murata", "yuki", "24", "20000201", "Japanese")
print(personal1.database)
personal1.setData("murata", "mizuki", "17", "20061019", "Japanese")
print(personal1.database)
print()


## CalcSquareクラス
## コンストラクタ：初期値（INT型）までのリストを作成する
## フィールド　　：
class CalcSquare:
    def __init__(self,num):
        self.numList = list(range(num + 1))
    
    def square(self):
        i = 0
        while i < len(self.numList):
            self.numList[i] = self.numList[i] ** 2
            i += 1
        return self.numList

class CalcSquareSummary(CalcSquare):

    def sum(self):
        result = 0
        for item in self.numList:
            result += item
        return result

num12 = CalcSquare(12)
print(num12.numList)
num12.name = "murata"
print(num12.name)
print(num12.square())
print(dir(CalcSquare))
print(dir(num12))
print()


num14 = CalcSquareSummary(14)
print(num14.numList)
print(num14.square())
print(num14.sum())

list14 = num14.numList