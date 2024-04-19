a = str(input())
textLength = len(a)
textReversed = ""
j=textLength
i=0
while i < textLength:
    textReversed+=a[j-1]
    i+=1
    j-=1

if a == textReversed:
    print("YES")
else:
    print("NO")