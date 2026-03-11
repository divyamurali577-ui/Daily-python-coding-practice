#positive or negative number
num=int(input("enter the number:"))
if (num>=1):
    print("positive number")
else:
    print("negative number")

#even or odd number
a=int(input("enter the number:"))
if (2%a==0):
    print("even number")
else:
    print("odd number")

#largest two number
a=int(input("enter the number:"))
b=int(input("enter the  number:"))
if(a>b):
    print("largest number")
else:
    print("smallest number")

#three largest numbers
a=int(input("enter the number:"))
b=int(input("enter the  number:"))
c=int(input("enter the  number:"))
if(a>b):
    print("largest number")
elif(a>c):
    print("largest number")
elif(b>c):
    print("largest number")
else:
    print("smallest number")
#divisible 5 and 11
a=int(input("enter the number:"))
if(a%5==0 and a%11==0):
    print("divisible by 5 and 11")
else:
    print("not divisible by 5 and 11")
#leap year
a=int(input("enter the year:"))
if(a%4==0):
    print("leap year")
else:
    print("not leap year")
#vowels
a=input("enter the characters:")
if(a=="a,e,i,o,u"):
     print("vowels")
else:
    print("consonants")
#multiple numbers3 and 7
a=int(input("enter the number:"))
if(a%3==0 and a%7==0):
    print("multiple of 3 and 7")
else:
    print("not multiple of 3 and 7 ")
#three digit number or not
a=int(input("enter the number:"))
if (a>100 and a<999):
    print("three digits no")
else:
    print("not three digits no")

a=int(input("enter the number:"))
if (a>100):
    print("greater than 100")
else:
    print("less than 100")