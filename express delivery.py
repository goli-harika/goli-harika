#expres delivery
weight=int(input("enter the weight:"))
if weight==4:
    print("the delivery can be expected within 24 hr..")
    if weight<=10:
        print("need to pay an extra amount for extra weight..")
    else:
        print("no need to pay any extra charge have a great delivery!!")
else:
    print("need to wait 3-5 business days to expect the delivery")
