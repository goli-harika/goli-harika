"""
tuples is a collection of itens/values/element
they are enclosed within the parathesisor
open brackets ()seperated by(,)
as tuples are imutable it mean we cant change
so when the data is fixed we can with tuples..
"""
#eg1
mytuple=(13,12,11)
print(type(mytuple))#<class tuple>
mytuple2=()#empty tuple
print(type(mytuple2))#<class tuple>
mytuple3=10
print(type(mytuple3))#<class int>
"""
note:when you wanna create a tuple with single values
it should be seperated but so that the compliert reats as tuple or else it just treat as integer
"""

#creation of tuple
#syntax:tuple variable=(val1,val2,val3..valn)
mytuple5=(12,13,23,45,34+78j,[12,34,45],"hello",(123,"ece"))
print(mytuple5)

#creating atuple with a single element
mytuple6=(55,)
print(type(mytuple6))

#creating the tiple with a list
h=[23,68.56,"kk"]
print(h)
r=tuple(h)

#creating the tuple with "tuple" predefined word
k=tuple()#it consider as empty tuple 
print(k)

#acesing the tuple in a list:using the index we can acess the element in a tuple
#index syntax(start:stop)
mytuple8=(12,13,22,44,55,(78,89),"hello")
print(type(mytuple8))
print(mytuple8[0:5])
print(mytuple8[0:3])

mytuple9=([12,13,14,15],(89,74,74))
print(mytuple9[1])

#slicing--it is used to retrive the elements from a particular range the 
# syntax(start:stop:skip)s^3
mytuple10=(11,12,44,55,88,99,"hello","ece","agri")
print(mytuple10[3:9:3])

mytuple11=(12,33,44,55,66,77,98,76,54,43,24,56,47)
print(mytuple11[4:10:5])

mytuple12=("hello",13,456,45,67,56+78j,"ists","ece","agri",345.9,"dept",12,23,34,56,67,90)
print(mytuple12[-1])
print(mytuple12[7:-2:2])
#note:index are of two type
#positive indexing or forward indexing :which are always starts with "0"from left hand side direction.
#negative indexing or backword indexing:which are always start with "-1"from right hand side direction


