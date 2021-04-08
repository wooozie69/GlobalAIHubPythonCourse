
def task1():
    myList = [1, 2, 3.1, 95, 98, 2000, "XP", "Vista", 7, 8.1, 10, True]
    tempList = []
    iterationCnt = int(len(myList) / 2)

    # myList before replacing first half with other half
    print("Before: ", end=" ")
    print(myList)
    
    for i in range(iterationCnt):
        tempList.append(myList[i])
        myList[i] = myList[i + iterationCnt]
    for i in range(iterationCnt):
        myList[i + iterationCnt] = tempList[i]

    # myList after rearranging
    print("After: ", end=" ")
    print(myList)

def task2():
    # Read a number first
    while (1):
        n = int(input("Please enter a single digit number: "))
        if n < 10 and n >= 0:
            break
        else:
            print("Incorrect entry")

    print("Even numbers from 0 to {}: ".format(n), end=" ")
    for i in range(n + 1):
        if i % 2 == 0:
                  print(i, end=" ")


task1()
print()
task2()
