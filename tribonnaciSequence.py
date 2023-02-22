from typing import List
def printTribRec(n) :
    if (n == 1 or n == 2 or n == 3) :
        return 1
    else :
        return (printTribRec(n - 1) +
                printTribRec(n - 2) +
                printTribRec(n - 3))

def tribonacci(num: int) -> List[int]:
    lst = []
    for i in range(1, num+1) :
        lst.append(printTribRec(i))
    return lst

inpt = input("Please enter the number you want to find the Tribonnaci sequence for: ")
print("The tribonnaci sequence of the given number is:", tribonacci(int(inpt)))