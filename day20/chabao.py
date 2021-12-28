from audioop import avg

data = ['a', 50, 91.1, (20, 1, 2)]
_, a, b, c = data
print(_)


def drop_first(gardes):
    first, *middle, last = gardes
    return sum(middle) / (len(gardes) - 2)


res = [100, 77, 99, 88, 44, 66, 11, 55, 22]


def maopao(res):
    for i in range(len(res) - 1):
        for j in range(len(res) - i - 1):
            if res[j] < res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res


print(maopao(res))
res2 = drop_first(res)
print(res2)

records = [("foo", 1, 2), ('bar', 'hello'), ('foo', 3, 4), ]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

for tag, *args in records:
    print(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
res3 = line.split(':')
print(res3)

a,*b,c = res3
print(a,type(a))
print(*b)

record2 = ('acme',50,134.45,(12,18,2018))
name,*num,(*_,year) = record2
print(year)

items = [1,10,7,4,5,9]
head,*tail = items
def adsum(i):
    h,*t=i
    return h+sum(t) if t else h

print(adsum(items))


dict1 = {'a':1,
    'b':{'c':'asdfghjklasdfghjkqwertyusdfghjdfghjdfghjkdfgh'},
        'd':2
    }


print(dict1.get('b').get('c'))

print(dict1['b']['c'])



