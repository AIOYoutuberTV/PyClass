temp = int(input())

if temp > 35 and temp >= 30:
    print("CANCEL SCHOOL")
elif temp > 30 and temp <= 35:
    print("CANCEL TWO CLASSES")
else:
    print("NORMAL CLASSES")