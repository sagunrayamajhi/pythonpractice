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
    list_of_divisor = []
    for i in range(1, number-1):
        if number % i == 0:
            list_of_divisor.append(i)
    if len(list_of_divisor) > 1:
        for value in list_of_divisor:
            print(value)
    else:
        print("Prime Number no divisors")

def getList(size) :
    listToReturn = []
    for i in range(0,size) :
        value = int(input("enter value"))
        listToReturn.append(value)
    return listToReturn

def giveCommonItems():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    size_of_first = int(input("Enter the size of first list"))
    first_list = getList(size_of_first)
    size_of_second = int(input("Enter the size of second list"))
    second_list = getList(size_of_second)
    newlist = list(set(a).intersection(set(b)))
    newlist.sort(reverse=True)  #when the original list isn't required this can be done, or sorted(list,reverse = true) when original list is required.
    newlist2 = sorted(list(set(a).difference(set(b))) + list(set(b).difference(set(a))))
    print("common items"+str(newlist))
    print("differnt items"+str(newlist2))
    print("Common in user list" +str(list(set(first_list).intersection(set(second_list)))))


def string_palindrome():
    input_string = input("enter String")
    if input_string == input_string[::-1]:  #Slicing
        print("palindrome")
    else:
        print("not palindrome")


def comprehenssion():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(list(filter(lambda x: x % 2 == 0, a)))


comprehenssion()


