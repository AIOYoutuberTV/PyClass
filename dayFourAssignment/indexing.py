def recieveArray(length,string): #e.g. 1 2 3 4 5 out: [1,2,3,4,5]
    out = []
    i=0
    j=0
    while i < len(string):

        if string[i] != " " and string[i+1] == " ": #is single digit
            out += string[i]
            i+=1
            j+=1
        elif string[i] != " " and string[i+1] != " ": #is not single digit
            buffer = ""
            k = 0
            while string[i] != " ":
                buffer += string[k]
                k+=1
                i+=1
            out[j]
            out[j] = int(buffer)
            del(buffer)
            del(k)
            j += 1
        else:
            i += 1
    return out

toUse = recieveArray(int(input()),str(input()))
print(toUse[int(input())])