treasure = [int(input()) , int(input()) , int(input())]

if treasure[0] < treasure[1] and treasure[0] < treasure[2]:
    print(treasure[1]+treasure[2])
elif treasure[0] > treasure[1] and treasure[0] < treasure[2]:
    print(treasure[0]+treasure[2])
else:
    print(treasure[0]+treasure[1])