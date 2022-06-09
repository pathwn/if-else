actual_cost=int(input("enter number"))
saleprice=int(input("enter number"))
if actual_cost>saleprice:
    print("loss")
elif saleprice>actual_cost:
    print("profit")
else:
    print("same price")    