try:
    val1=int(input("Value 1: Enter a number : "))
except:
    print("Error: Value 3 is not a number")
    print("Handling by using 0 as number")
    val1 = 0
    raise SystemExit("Error occured in value 1")

try:
    val2=int(input("Value 2: Enter a number : "))
except: 
    val2 = 0
    print("Error: Value 3 is not a number")
    print("Handling by using 0 as number")
    raise SystemExit("Error occured in value 2")
    

try:
    val3=int(input("Value 3: Enter a number : "))
except:
    print("Error: Value 3 is not a number")
    print("Handling by using 0 as number")
    val3 = 0
    raise SystemExit("Error occured in value 3")

# crtl + ~ --> window to open the code terminal


def add(val1,val2):
    c=val1+val2
    print("Result of adddition is : ", c)
    return c

print("Running add function with values: ", val1, " and ", val2)
ans = add(val1, val2)
print("Add function executed successfully ")

print("Running add function with values: ", ans, " and ", val3)
add(ans, val3)
print("Add function executed successfully ")

