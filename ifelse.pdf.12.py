month=input("enter month")
if month=="jan" or month=="mar" or month=="may" or month=="july" or month=="aug" or month=="out" or month=="decem":
    print("31 day month")
elif month=="april" or month=="june" or month=="sep" or month=="novem":
    print("30 day in month")
else:
    print("28 day in month")        