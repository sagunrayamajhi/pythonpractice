from getpass import getpass

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


def rock_paper_scissors():
    check = 1 ;
    rock = 1;
    paper=2;
    scissors=3;
    # while check == 1:
    print("1. Rock \n 2. Paper \n 3. Scissors")
    # player1 = int(input("Player 1 choose your option"))
    player1 = int(getpass("Player 1 choose your option"))
    # player2 = int(input("Player 2 choose your option"))
    player2 = int(getpass("Player 2 choose your option"))
    if (player1+1) % 4 > (player2+1) % 4:
        print("Player 1 wins")
    elif (player1+1) % 4 < (player2 + 1) % 4:
        print("Player 2 wins")
    else:
        print("draw")

def fileExtension():
    fileName = input("Enter file name")
    if("." in fileName ):
        ext = fileName.split(".")[-1]
        print(ext)
    else:
        print("Not a valid file")

def getFirstandLastValue():
    a = ["a", "b", "c"]
    print(a[0] +"\t" + a[-1])

def examDate():
    exam_st_date = (11, 12, 2014)
    val = 0
    for i in exam_st_date:
        if (not len(exam_st_date) == val) :
            print(str(i)+"/", end="")
        else:
            print(str(i))

def pract():
    list1 = ['a', 'b', 'c']
    tup = (1,2,3,4)
    for index,value in enumerate(tup, start=5):
        print(value,index)

def dict_test():
    subject = {"name": "ABC", "Age": 21, "Smoker": True}
    pp= pprint.PrettyPrinter(indent=4)
    pp.pprint(subject)

contact={
    "ABC":'1234',
    "CDE":'23434'
}

def getContact():
    print(contact.get(input("Enter name"),"NOT FOUND"))


def choice1():
    print("Choice 1")

def choice2():
    print("Choice 2")

def default():
    print("DEFAULT")


opt = {
    "1": choice1,
    "2": choice2
}


def dictTest():
    inp = input("Enter value")
    opt.get(inp,default)()


def testDefArgm(val1 = "Hello", val2 = "World"):
    print(val1+" "+val2)


testDefArgm()
testDefArgm("Goodbye")



