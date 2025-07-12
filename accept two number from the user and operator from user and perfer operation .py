num1=int(input("enter a number.."))
num2=int(input("enter a number.."))
opr=input("enter a operator:")
if opr=="+":
    print("the answer :",num1+num2)
elif opr=="-":
    print("the answer:",num1-num2)
elif opr=="*":
    print("the answer:",num1*num2)
elif opr=="/":
    print("the answer:",num1/num2)
else:
    print("wrong operator selected..")