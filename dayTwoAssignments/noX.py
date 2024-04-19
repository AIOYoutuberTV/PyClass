text = str(input())
result = ""
i=0
while i < len(text):
    if text[i] != "x":
        result += text[i]
    i+=1
print(result)
