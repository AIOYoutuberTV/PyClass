text = input()
textMid = len(text)//2
result = ""
i=0
while i != len(text):
    if i < textMid:
        result += text[i+textMid]
        i += 1
    else:
        result += text[i-textMid]
        i += 1
print(result)