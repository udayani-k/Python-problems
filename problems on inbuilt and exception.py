print(bin(7))
print(pow(3,2))
print(abs(-99))
#
for i,c in enumerate("AB",start=1):
    print(i,c)
#
a=["suresh","rajesh","mahesh"]
b=enumerate(a)
print(b)
print(list(a))
#
print(list(map(abs,[-1,2,-3])))
#
try:
    print(int("12a"))
except ValueError:
    print("Invalid")
finally:
    print("End")

#
def think(x):
    return x*3
a=[1,2,3,4,5]
result=map(think,a)
print(result)
print(list(result))
#
a=["Apple","Mango","Banana"]
b=enumerate(a)
print(b)
print(list(b))
#
a = int("20")
print(a)

b = int("10")
print(b)

try:
    print(a / b)
except ValueError:
    print("please enter a valid number")

#
items=[10,20,30]
try:
    print(items[10])
except IndexError:
    print("sorry,that index does not exist")

#
try:
    print(10)
except:
    print(hello)
else:
    print("hi")
finally:
    print("wrong")

# difference between else and finnaly
""" else:runs only if there is no error
  finally:always runs, error or not"""

   
    
