print("python")
a=["a","n","d"] #a="and"
print(a)

'''

int        char      float
----------------------------
long       string    double #可以記錄小數點很多的位數, float無法
short
boolean

'''

#Loop 
#for loop and while loop
'''
for loop 明確知道迴圈要跑幾次
#for "a variable" in "list":
    "your code"
example: for i in range (0,3):
    print(i)
'''

'''
while loop 不知道迴圈要跑幾次
#while "condition":
    "your code"
example; while true:
    print("It's true")
'''
a=3
b=10
c=8
while a<b and c>a:
    print("In loop")
    a=a+1

#break 強行把迴圈停止
#continue 提早結束迴圈 直接跑下一輪迴圈 
print("      ")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("      ")

name="Janice" #escape character
name="Janice\nAndrew"
print(name)
print("-----------------------")
name="Janice\tAndrew"
print(name)

#if statement
'''
#if "boolean condition":
    "your code"
'''

a == "Andrew"
if a== "Andrew":
    print("Valid name")
else:
    print("Valide name")

#elif -> the same as "else", but can have multiple 
# the statement that have elif will also only have 1 result, the first that fit condition will be printed

print("-----------------------------------------------------------------------------------------------------------------")
'''
switch case
# match "variable":
    case "a":
        "your code" 
    case "b":
        "your code"
    ...
'''
product="pencil"

match product:
    case "pencil":
        print("pencil")
    case "book":
        print("book")
    case "tank":
        print ("tank")

