#Write a program that prints all Armstrong numbers within a specified range using loops and conditional statements.
lower = int(input())
upper = int(input())
for num in range(lower,upper+1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum =sum+ digit ** order
       temp //= 10
   if num == sum:
       print(num)
