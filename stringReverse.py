def stringReverse(a):
    j=len(a)
    out=""

    i=0
    while i < len(a):
        out += a[j-1]
        j -= 1
        i += 1
    return(out)