"""
def reverse_order():
    list = [1, 2, 3, 4, 5]
    answeer = list[::-1]
    
    count = len(list)
    for _ in range(len(list)):
        answeer.append(list[count-1])
        count -= 1
    
    print(answeer)

def even_list():
    list = []
    answeer = []
    n = int(input("Enter the size of the liss: "))

    for i in range(n):
        element = int(input())
        list.append(element)

    for i in list:
        if i % 2 == 0:
            answeer.append(i)

    print(answeer)

def comon_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    answeer = []

    for i in list1:
        for j in list2:
            if i == j and i not in answeer:
                answeer.append(i)
    print(answeer)


def longest_string():
    list = ["apple", "banana", "orange", "kiwi"]
    biggest = ""
    for i in list:
        if len(i) > len(biggest):
            biggest=i

    print(biggest)

def list_sum():
    list = [1, 2, 3, 4, 5]
    sum = 0
    for i in list:
        sum += i
    print(sum)
"""

def reverse_order():
    lst = [1, 2, 3, 4, 5]
    result = lst[::-1]
    print(result)

def even_list():
    n = int(input("Enter the size of the list: "))
    lst = []

    for _ in range(n):
        element = int(input("Enter an element: "))
        lst.append(element)

    result = [num for num in lst if num % 2 == 0]
    print(result)

def common_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    result = list(set(list1) & set(list2))
    print(result)


def longest_string():
    lst = ["apple", "banana", "orange", "kiwi"]
    result = max(lst, key=len)
    print(result)

def list_sum():
    lst = [1, 2, 3, 4, 5]
    result = sum(lst)
    print(result)



# reverse_order()
# even_list()
# common_elements()
# longest_string()
# list_sum()


#reverse_order()
#even_list()
#comon_elements()
#longest_string()
#list_sum()