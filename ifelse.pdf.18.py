phy=int(input("enter marks"))
che=int(input("enter marks"))
bio=int(input("enter marks"))
math=int(input("enter marks"))
com=int(input("enter marks"))
total=phy+che+bio+math+com
percentage=total*100/500
if percentage>=90:
    print("grade A")
elif percentage>=80:
    print("grade B") 
elif percentage>=70:
    print("grade C")
elif percentage>=60:
    print("grade D")
elif percentage>=40:
    print("grade E")
else:
    print("grade F")                   