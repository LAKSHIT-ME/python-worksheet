# print the following

print("Twinkle,Twinkle, little star.")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")
print("Twinkle,Twinkle, little star.")
print("How I wonder what you are!")



# First name and last name

fname = input("Enter first name:")
lname = input("Enter last name: ")
print(lname,fname)



# Area of circle

r = int(input("Enter the radius : "))
area = 3.14*r*r
print(area)



# First and the last

color = ["red","green","white","black"]
print(color[0])
print(color[3])



# n + nn +nnn

n = int(input("Enter the number: "))
ones = n
tens = n*10 + ones
hundreds = n*100 + tens
add = ones + tens + hundreds
print(add)



# comma seperated and tuple

x = str(input("Enter the number: ")).split(",")
print(x)
x = tuple(x)
print(x)



# celcious to farehnite

celsius = float(input("Enetr temperature: "))
fahrenheit = 1.8*celsius + 32
print(fahrenheit)




# swap the numbers

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
temp = first
first = second
second = temp

print(first,second)




# odd or even

n = int(input("Enter the number: "))
if (n%2 == 0) : print("even number.")
else : print("odd number.")



# leap year or not

year = int(input("Enter the year"))

if (year % 400 == 0) and (year % 100 == 0):
    print("is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print("is a leap year")
else:
    print("is not a leap year")


# distance formula


x1,y1 = int(input("x1:")), int(input("y1:"))
x2,y2 = int(input("x2:")), int(input("y2:"))
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(distance)



# triangle or not

a1, a2, a3 = float(input("a1:")),float(input("a2:")),float(input("a3:"))
sum = a1 + a2 + a3
if (sum == 180) : print("This is a triangle.")
else : print("This is not a triangle.")



# compound interset

p ,r ,t,n  = int(input("principle: ")), int(input("rate: ")), int(input("time: ")), int(input(number of time))
CI = p*((1+(r/n))**(t*n))
print(CI)



# prime or not

N = int(input("Enter the number : "))
c = 0
for i in range (2,N):
if(N % i == 0) :
c = c + 1
if c > 0:
print("Not Prime")
else:
print("Prime")


# N to 12+22+33....N2

n = int(input("Enter the number: "))
sum = 0
for i in range(1,n+1) :
sum = sum + i**2
print(sum)
