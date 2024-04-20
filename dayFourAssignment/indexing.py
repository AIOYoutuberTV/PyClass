def recieveArray(length,string): #e.g. 1 2 3 4 5 out: [1,2,3,4,5]
    i=0
    out = []
    while i < len(string):
        if string[i] != " ":
            out += string[i]
            i+=1
        else:
            i+=1
    return out


toUse = recieveArray(int(input()),str(input()))
print(toUse[int(input())])