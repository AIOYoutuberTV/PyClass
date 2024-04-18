score = int(input())

Emergance = range(0,41)
Developing = range(41,81)
Achieved = range(81,101)

if score in Emergance:
    print("Emerging")
elif score in Developing:
    print("Developing")
elif score in Achieved:
    print("Achieved")
else:
    print("Err: value undefined")