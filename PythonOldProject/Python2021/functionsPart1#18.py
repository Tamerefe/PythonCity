# def <fonksiyon ismi> (<argümanlar>)   # snake_case
# """
# Bu kod ne ise yarar                   # docstring
# """
# '''                                   # return/print

def printIt():
    """
    Whatever you write here will be invisible 
    """
    print("printt")

printIt()

print(printIt())

print("")

def pleaseReplayToMe():
    return print("replayy")


pleaseReplayToMe()
print(pleaseReplayToMe())

print("")

def returNum(num):
    return num 

print(returNum(5))


def returNum2(num2 = 35):
    return num2


print(returNum2())
print(returNum2(85))

print("")

def bigNumRep(a, b):
    if a > b:
        return print(a)
    elif b > a:
        return print(b)

bigNumRep(25, 35)
bigNumRep(125, 65)
