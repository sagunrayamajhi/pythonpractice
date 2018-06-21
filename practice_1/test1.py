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


def decending():
    li = [3, 1, 2, 6, 7, 8, 9]
    li.sort(reverse=True)
    print(li)

def multidimension():
    mylist = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]
    for list in mylist:
        for innerlist in list:
            if int(innerlist) % 2 == 1:
                print(innerlist)

def Salary():
    salary = [15000, 20000, 17000, 18900, 30000]
    new_salary=[]
    for value in salary:
        new_salary.append(value + 23*value/100)

    print(new_salary)

def maxMin():
    my_list = [4, 2, 4, 2, 4, 5, 7, 8, 9, 23, 8, 5, 4, 2, 2, 34, 4, 45]
    maxm = minm = my_list[0]
    for val in my_list:

        if maxm < val:
            maxm = val
        if minm > val:
            minm = val
    print("Minimum: "+ str(maxm) +" Maximum: " + str(minm))

def makeCube(list_tobe_cubed):
    cubes=[]
    for each in list_tobe_cubed:
        cubes.append(each**3)
    return cubes

arbitary_list = [1, 2, 4, 4, 3, 5, 6]
#print(makeCube(arbitary_list))

def slopeintercept(list):
    m = int(input("Enter value of m"))
    c = int(input("Enter value of c"))
    for val in list:
        out = str(m*int(val) + c)
        print(out)


#slopeintercept(arbitary_list)

##Write a function that prompts user to input his/her full name.
# After user enter's his/her full name, split it and store it in variables first_name and last_name.
# (hint: use string's split method. Also handle condition for his/her middle name as well)

def namesplit(name):
    print(type(name.split(" ")))
    if(len(name.split(" ")) ==2):
        first = name.split(" ")[0]
        last = name.split(" ")[1]
        print("First name: {}".format(first))
        print("Last name :" + last)
    elif(len(name.split(" ")) ==3):
        first = name.split(" ")[0]
        middle = name.split(" ")[1]
        last = name.split(" ")[2]
        print("First name :" + first)
        print("Middle name :" + middle)
        print("Last name :" + last)
    else:
        print("Invalid name")

namesplit("Ram KC")

def sum(num1,num2):
    total = num1 + num2
    print("{}+{}={}".format(num1,num2,total))


#print(sum(1,2))

##Write a program to generate following output.
#>>> What's your name?
#Nice to meet you ! ****
#>>> Your age?
#So, you are already **** years old, ****!

