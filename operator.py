# arithmetic operator
a = int(input("enter a number: "))
b = int(input("enter a number: "))
print("the addition ", a+b)
print("thesubtraction", a-b)
print("the multiplication", a*b)
print("the division", a/b)
print("the floor division", a//b)
print("the power",a**b)
# bit wise operator
a= 9
b = 4
c = a&b
print("And operator")
print(c)
d=15
e=13
f=d|e
print(f)
g=12
h=14
i=g^h
print(i)
#relation and comparison operator
a=int(input("enter a nmber:"))
b=int(input("enter a number:"))
print("the greater values",a>b)
print("the lesser values",a<b)
print("the greater than or equal too value",a>=b)
print("the lesser than or equal too value",a<=b)
print("the equal too values",a==b)
print("the not equal too value",a!=b)
#identity operator    
x=(1,2,3)
y=(4,5,6)
z=x
print(x in y)
print(x is z)
print(y is z)
print(y is not z)
print(z is not x)
print(x is not y)
#logical operator
a=13
b=45
c=a>=34 and b==50
print(c)
b=67
d=89
f=b!=67 or d==89
print(f)
a=10
print(not(a))
b=0
print(not(b)) 
#member ship operator
x=["apple","banana",]
print("apple" in x)
print("pp" not in x)
print("banana" not in x)
print("dragon" in x)