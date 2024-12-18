
class Cash :
    def __init__(self, a,b, number):
        self.a = a
        self.b = b
        self.number = number
    
    @staticmethod
    def create(dict):
        cfs = []
        number = 0
        for value in dict.values():
            print(value)
            cf = Cash(value['a'],value['b'] , number)
            cfs.append(cf)
            number +=1
        return cfs        

a1 = dict(a=0, b=0)
a2 = dict(a=1,b=2)
a3 = dict(a=2,b=2)
all = dict(cf1 = a1, cf2 = a2, cf3 = a3)

cfs = Cash.create(all)
print(cfs)

cf_a_list = []
for cf in cfs:
    cf_a_list.append(cf.number)
    print(f'a: {cf.a} , b: {cf.b} , number: {cf.number} ')
    print(cf_a_list)

list0 = ['USD','JPY','USD','AUD']
list = ['USD','JPY','USD','AUD','JPY','USD','JPY','AUD','JPY','AUD']
set1 = set()
for item in list:
    set1.add(item)
print(list)
print(set1)

for item in set1 :
    i = 0
    count = 0
    while i < len(list0) :
        if list0[i] == item :
            count +=1
        i += 1
    print(item)
    print(count)



