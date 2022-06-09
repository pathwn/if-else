day=int(input("enter day"))
if day>=1 and day<=5:
    charge=day*2
    print(charge)
elif day>=6 and day<=10:
    charge=day*3
    print(charge)
elif day>=10 and day<=15:
    charge=day*4
    print(charge)
elif day>15:
    charge=day*5
    print(charge)
else:
    print("none")                