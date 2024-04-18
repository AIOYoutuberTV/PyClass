treasure = [int(input()) , int(input()) , int(input())]

i = 0
rm1 = 0
rm2 = 0
while i < len(treasure):
    if rm1 < treasure[i]:
        rm2 = rm1
        rm1 = treasure[i]
    elif rm2 < treasure[i]:
        rm2 = treasure[i]
    else:
        break
    i += 1
#Why am I manually managing each va7r like I'm working with register in assembly? 
print(rm1+rm2)