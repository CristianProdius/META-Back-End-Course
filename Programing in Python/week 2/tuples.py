def concatinate():
    tuple1= (1, "best", 5.4)
    tuple2= (1, "dude", 5.4)
    print(*tuple1, *tuple2)

def max_num():
    tuple1 = (5, 2, 9, 1, 7)
    print(max(tuple1))

def odd_tuple():
    tuple1 = ("apple", "banana", "kiwi", "orange", "mango")
    output = [i for i in tuple1 if len(i)%2==1]
    print(output)

def alphabetic():
    tuple1 =  ("John", "Alice", "Bob", "David")
    output = sorted(tuple1)
    print(output)

def square():
    tuple1 = (1, 2, 3, 4, 5)
    output = tuple(num**2 for num in tuple1)
    print(output)


concatinate()
max_num()
odd_tuple()
alphabetic()
square()