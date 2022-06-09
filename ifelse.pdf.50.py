month=input("enter month")
day=int(input("enter day"))
if month in ("dacember","january","february"):
    if day>=1 and day<=31:
        print("winter")
    else:
        print("not a winter")
elif month in ("march","april","may"):
    if day>=1 and day<=30:
        print("spring")
    else:
        print("not a spring")
elif month in ("june","july","august",):
    if day>=1 and day<=31:
        print("summer") 
    else:
        print("not a summer")
elif month in ("september","october","november"):
    if day>=1 and day<=30:
        print("autumn")
    else:
        print("none")                                             