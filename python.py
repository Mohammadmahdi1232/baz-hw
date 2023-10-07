# import math

#29:    ezafe        if
# a=int(input())
# if a%3==0 and a%10!=0 or (a*a)%8==0:
#     print('yes')
#______________________________________________________________
#30:    ezafe
# a=int(input())
# b=int(input())
# dahgan_a=(a//10)%10
# dahgan_b=(b//10)%10
# jam=dahgan_a+dahgan_b
# if jam>5:
#     print('yes')
#______________________________________________________________
#31:    ezafe
# a=int(input())
# b=int(input())
# yekan_a=a%10
# yekan_b=b%10
# if yekan_a%yekan_b==0:
#     print('yes')
#______________________________________________________________
#32:    ezafe
# a=int(input())
# b=int(input())
# yekan_a=a%10
# sadgan_a=a//100
# dahgan_b=(b//10)%10
# if sadgan_a%dahgan_b!=0 or yekan_a%2==0:
#     print('yes')
#______________________________________________________________
#33:    ezafe
# a=int(input())
# b=int(input())
# c=int(input())
# if a+b>c:
#     print('yes')
# elif a+c>b:
#     print('yes')
# elif b+c>a:
#     print('yes')
# else:
#     print('no')
#______________________________________________________________
#34:    ezafe
# a=int(input())
# b=int(input())
# c=int(input())
# if a==b and b==c :
#     print('yes')
# else:
#     print('no')














##---------------------------------------------------------------
#36:    1     if
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b>c:
#     print(a)
# elif a>c>b:
#     print(a)
# elif b>a>c:
#     print(b)
# elif b>c>a:
#     print(b)
# elif c>a>b:
#     print(c)
# elif c>b>a:
#     print(c)
#______________________________________________________________
#37:    2     if
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b>c:
#     print(a,b,c)
# elif a>c>b:
#     print(a,c,b)
# elif b>a>c:
#     print(b,a,c)
# elif b>c>a:
#     print(b,c,a)
# elif c>a>b:
#     print(c,a,b)
# elif c>b>a:
#     print(c,b,a)
#______________________________________________________________
#38:    3     if
# a=int(input())
# if 1<=a<=7:
#     print(1)
# elif 8<=a<=15:
#     print(2)
# elif 16<=a<=23:
#     print(3)
# elif 24<=a<=30:
#     print(4)
# else:
#     print('Enter the numbers 1-30')
#______________________________________________________________
#39:    4     if
# a=input()
# for i in a:
#     if i!='0':
#         print(i)
#______________________________________________________________
#40:    5    if
# q=int(input())
# a1=q%10
# b1=q/10
# a2=b1%10
# b2=b1/10
# a3=b2%10
# b3=b2/10
# javab_1=(a1*1)+(a2*2)+(a3*4)

# q2=int(input())
# a1=q2%10
# b1=q2/10
# a2=b1%10
# b2=b1/10
# a3=b2%10
# b3=b2/10
# javab_2=(a1*1)+(a2*2)+(a3*4)
# b=javab_1+javab_2
# print(b)   


##javabe too:
# a=input()
# b=input()
# s=bin(int(a,2)+int(b,2))[2:]
# print(s)






















##---------------------------------------------------------------
#66:    1   loop:
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def is_fibonacci(n):
#     a, b = 0, 1
#     while b < n:
#         a, b = b, a + b
#     return b == n

# count = 0
# for _ in range(100):
#     num = int(input("adad ra vared kon : "))
#     if is_prime(num) and is_fibonacci(num):
#         count += 1

# print(" ham aval ham fibonacci :", count)

#______________________________________________________________
#67:    2   loop:
# def is_divisible(n, num):
#     a, b = 0, 1
#     while b < n:
#         if b % num == 0:
#             return True
#         a, b = b, a + b
#     return False

# num = int(input("adad ra vared kon: "))
# count = 0
# for i in range(1, num + 1):
#     if is_divisible(i, num):
#         count += 1

# print("Number of Fibonacci numbers divisible by", num, ":", count)

#______________________________________________________________
#68:    3   loop:
# a=input()
# s=0
# for i in a:
#     if i=='0':
#         s=s+1        
# print(s)
#______________________________________________________________
#69:    4   loop:
# a=input()
# s=0
# for i in a:
#     if i=='0':
#         b=a.replace('0','')   
# print(b) 

#// and code 2:
# a=int(input())
# sa=str(a)
# b=sa.replace('0','')
# int_a=int(b)
# print(int_a)
#______________________________________________________________
#70:    5   loop:
# a=[]
# b=[]
# def n():
#     for i in range(56,1984,1):
#         for m in range(1,i):
#             if i%m==0:
#                 print(str(n)+' maghsoom elaih : '+str(m))
# n()





















##---------------------------------------------------------------
# 86:    1   arry
# s=0
# n=int(input(' chand adad mikhaiy vared kony? : '))
# for i in range(n):
#     a=int(input())
#     if a>s:
#         s=a
# print(s)
#______________________________________________________________
# 87:    2   arry
# n=int(input(' chand adad mikhaiy vared kony? : '))
# arry=[]
# for i in range(n):
#     a=int(input())
#     arry.append(a)
# arry.sort(reverse=True)
# print(arry)
#______________________________________________________________
# 88:    3   arry
# n=int(input(' chand adad mikhaiy vared kony? : '))
# arry=[]
# for i in range(n):
#     a=int(input())
#     arry.append(a)
# b=sorted(arry)
# if b==arry:
#         print('yes adad az koochak be bozorg hast')
# else:
#         print('no adad az koochak be bozorg nist')
#______________________________________________________________
# 89:    4   arry
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# numbers = []
# for _ in range(10):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# result = []
# for num in numbers:
#     if not is_prime(num):
#         result.append(num)

# print("Numbers without prime numbers:", result)
                
#______________________________________________________________
# 90:    5   arry
# n=int(input(' chand adad mikhaiy vared kony? : '))
# arry=[]
# for i in range(n):
#         a=int(input())
#         print(f'{a} : {math.factorial(a)}')


 
























##---------------------------------------------------------------
#106:  1  def
# def zoj():
#     sum=0
#     for i in range(5):
#         a=int(input())
#         if a%2==0:
#             sum=sum+1
#     print(sum)

# zoj()
#______________________________________________________________
#107:   2   def
# def mian(a,b,c,d,e):
#     miangin:(a+b+c+d+e)/5
#     if a+3 or a-3==miangin:
#         print(a)
#     if b+3 or b-3==miangin:
#         print(b)
#     if c+3 or c-3==miangin:
#         print(c)
#     if d+3 or d-3==miangin:
#         print(d)
#     if e+3 or e-3==miangin:
#         print(e)
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# mian(a,b,c,d,e)
#______________________________________________________________
#108:   3   def
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def count_primes(numbers):
#     count = 0
#     for number in numbers:
#         if is_prime(number):
#             count += 1
#     return count
# numbers = []
# for i in range(10):
#     a=int(input())
#     numbers.append(a)
# print(count_primes(numbers))

#______________________________________________________________
#109:   4   def
# def factorial():
#     s=0
#     while s<100:
#         a=int(input())
#         print(math.factorial(a))
# factorial()
#______________________________________________________________
#110:   5   def  
# def sort():
#     arry=[]
#     n=int(input('chand adad mikhahi vared koni? : '))
#     for i in range(n):
#         a=int(input())
#         arry.append(a)
#     arry.sort(reverse=True)
#     print(arry)
# sort()
























#---------------------------------------------------------------
#117:   1    string
# a=input()
# na=a.title()
# print(na)
#______________________________________________________________
#118:   2
# a=input()
# for i in a:
#     if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
#        print(i)
#______________________________________________________________
#119:   3   string
# a=input()
# na=a.replace('a','')
# print(na)
#______________________________________________________________
#120:   4    string  
# a=input()
# na=a.replace(' ','')
# print(na)
#______________________________________________________________
# 121:   5   string
# a=int(input())
# b=int(input())
# print(a+b)       


