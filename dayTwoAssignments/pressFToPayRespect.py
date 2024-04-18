word = str(input())
wordLength = len(word)
i = 0
fCount = 0

while i != wordLength:
    if word[i] == "f":
        fCount += 1
        i += 1
    else:
        i += 1
print(fCount)