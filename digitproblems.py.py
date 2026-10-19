# #it is used to print the last number in an element by using the % (modulus) Operator and also by number 10 it compulsory and it is a formula for finding the last digit of a number
# n=int(input("Enter a number:"))
# print(n%10)

# #it is used to print the number except the last digit by using the // (floor division) Operator and also by number 10 it compulsory and it is a formula for finding all digits except the last one
# num=int(input("Enter a number:"))
# print(num//10)

# #counting the even and odd numbers in a given range
# n = int(input("Enter a number: "))

# even = 0
# odd = 0

# while n > 0:
#     digit = n % 10

#     if digit % 2 == 0:
#         even += 1
#     else:
#         odd += 1

#     n = n // 10

# print(even, odd)

# #sum of even numbers in a given range
# n=int(input("enter a number:"))
# total=0
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         total+=digit
#         n=n//10
#         print(total)

# #sum of odd numbers in agiven range
# n = int(input("Enter a number: "))
# total = 0

# while n > 0:
#     digit = n % 10

#     if digit % 2 != 0:
#         total += 1

#     n = n // 10

# print(total)


# #sum of the first and last digit of a number
# num=int(input("enter a number:"))
# last=num%10
# while num>=10:
#     num=num//10
# first=num
# print(first+last)

# #finding the biggest numebr and the samllest number n a given range
# n=int(input("Enter a number:"))
# big=0
# small=0
# while n>0:
#     digit=n%10
#     if digit>=5:
#         big=big+1
#     else:
#         small=small+1
#         n=n//10
#         print(big,small)

#sum of odd numbers in a given range
n=int(input("enter a number:"))
total=0
while n>0:
    digit=n%10
    if digit%2==0:
      total=total+digit
      n=n//10
      print(total)

#Balanced number
n=int(input("Enter a number:"))
even=0
odd=0
while n>=0: 
   digit=n%10
   if digit%2==0:
      even=even+1
   else:
      n=n//10
      odd=odd+1
if even==odd:
   print("yes")
else:
   print("no")
      
   

