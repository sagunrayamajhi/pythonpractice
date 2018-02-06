def first():
    i = int(input("Number:"))
    listexample = [1, 2, 3, 4, 5, 6, 7]
    listout = []
    for value in listexample:
        if value > i:
            listout.append(value)
    for value in listout:
        print(value)


def divisor():
    number = int(input("Enter a number"))
    list_of_divisor=[]
    for i in range(1, number-1):
        if number % i == 0:
            list_of_divisor.append(i)
    if len(list_of_divisor) > 1:
        for value in list_of_divisor:
            print(value)
    else:
        print("Prime Number no divisors")

def removeDuplicateitems():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    newlist=[]


