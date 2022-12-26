loop = True
list = []  
n = int(input("Enter No of Student: "))
count = 1
   
for i in range(n):
    marks = int(input(f"Enter marks for student {count}: "))
    list.append(marks)
    count+=1
    
def absentSC(list, n):
    abs = 0
    for i in range(n):
        if list[i]==0:
            abs +=1
    return abs      

def maxMarks(list, n):
    max = 0
    for i in range(n):
        if max<list[i]:
            max = list[i]

    return max

def largestMFreq(n, list):
    mfreq = 0
    check = maxMarks(list, n)
   
    for i in range(n):
        if check == list[i]:
            mfreq += 1
    return mfreq


def minMFreq(n, list):
    freq = 0
    check = minMarks(list, n)
   
    for i in range(n):
        if check == list[i]:
            freq += 1
    return freq

def minMarks(list, n):
    min = list[0]
    for i in range(n):
        if min>list[i]:
            min = list[i]

    return min
   
   
def averageOfMarks(list, n):
    sumInitialize = 0
    for i in range(n):
        sumInitialize += list[i]

    return (sumInitialize/n)



def showList():
    print("--------------------Select Your Choice From Following list-----------------\n1) Enter 1 for Average\n2) Enter 2 for Maximum\n3) Enter 3 for Minimum\n4)Enter 4 for Largest Marks Frequency\n5)Enter 5 for minimum Marks Frequency\n6)Enter 6 for Count of absent student\n7) Enter 7 to create new list of marks\n8) Enter 8 to exit")
showList()

while loop:
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Average marks obtained by student is:",averageOfMarks(list, n))
       
    elif choice == "2":
        print("Maximum marks obtained by student is: ",maxMarks(list, n))
       
    elif choice == "3":
        print("Minimum marks obtained by student is: ",minMarks(list, n))
       
    elif choice == "4":
        print(f"{maxMarks(list, n)} is largest marks and its frequency is: ",largestMFreq(n, list))
       
    elif choice == "5":
        print(minMarks(list, n), " is minimum marks and its frequency is: ",minMFreq(n, list))
       
    elif choice == "6":
        print("Number of absent student are: ", absentSC(list, n))
       
    elif choice == "7":
        print("New list creataed")
        list = []

        n = int(input("Enter No of Student: "))
        count = 1
   
        for i in range(n):
            marks = int(input(f"Enter marks for student {count}: "))
            list.append(marks)
            count+=1
        print("--------------------Select Your Choice From Following list-----------------\n1) Enter 1 for Average\n2) Enter 2 for Maximum\n3) Enter 3 for Minimum\n4)Enter 4 for Largest Marks Frequency\n5)Enter 5 for minimum Marks Frequency\n6)Enter 6 for Count of absent student\n7) Enter 7 to create new list of marks\n8) Enter 8 to exit")
    elif choice == "8":
        loop = False
    else:
        print("You entered wrong choice try again")
	
	