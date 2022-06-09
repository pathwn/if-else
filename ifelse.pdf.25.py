working_day=int(input("enter working_day"))
attendange=int(input("enter attendange"))
percentage=attendange/working_day*100
if percentage<75:
    print("not allowed")
else:
    print("allowed")    