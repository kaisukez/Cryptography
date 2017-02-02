def printText(Text):
    print('    ', end='')
    for char in Text:
        print(char, end='')
    print('')

cipherText = input('Enter Cipher Text\n    ')

#find letter frequency
a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=0
for num in range(len(cipherText)):
    if cipherText[num] == 'a' or cipherText[num] == 'A':
        a += 1
    elif cipherText[num] == 'b' or cipherText[num] == 'B':
        b += 1
    elif cipherText[num] == 'c' or cipherText[num] == 'C':
        c += 1
    elif cipherText[num] == 'd' or cipherText[num] == 'D':
        d += 1
    elif cipherText[num] == 'e' or cipherText[num] == 'E':
        e += 1
    elif cipherText[num] == 'f' or cipherText[num] == 'F':
        f += 1
    elif cipherText[num] == 'g' or cipherText[num] == 'G':
        g += 1
    elif cipherText[num] == 'h' or cipherText[num] == 'H':
        h += 1
    elif cipherText[num] == 'i' or cipherText[num] == 'I':
        i += 1
    elif cipherText[num] == 'j' or cipherText[num] == 'J':
        j += 1
    elif cipherText[num] == 'k' or cipherText[num] == 'K':
        k += 1
    elif cipherText[num] == 'l' or cipherText[num] == 'L':
        l += 1
    elif cipherText[num] == 'm' or cipherText[num] == 'M':
        m += 1
    elif cipherText[num] == 'n' or cipherText[num] == 'N':
        n += 1
    elif cipherText[num] == 'o' or cipherText[num] == 'O':
        o += 1
    elif cipherText[num] == 'p' or cipherText[num] == 'P':
        p += 1
    elif cipherText[num] == 'q' or cipherText[num] == 'Q':
        q += 1
    elif cipherText[num] == 'r' or cipherText[num] == 'R':
        r += 1
    elif cipherText[num] == 's' or cipherText[num] == 'S':
        s += 1
    elif cipherText[num] == 't' or cipherText[num] == 'T':
        t += 1
    elif cipherText[num] == 'u' or cipherText[num] == 'U':
        u += 1
    elif cipherText[num] == 'v' or cipherText[num] == 'V':
        v += 1
    elif cipherText[num] == 'w' or cipherText[num] == 'W':
        w += 1
    elif cipherText[num] == 'x' or cipherText[num] == 'X':
        x += 1
    elif cipherText[num] == 'y' or cipherText[num] == 'Y':
        y += 1
    elif cipherText[num] == 'z' or cipherText[num] == 'Z':
        z += 1

sampleStat = [['a','A',a],['b','B',b],['c','C',c],['d','D',d],['e','E',e],['f','F',f],['g','G',g],['h','H',h],['i','I',i],['j','J',j],['k','K',k],['l','L',l],['m','M',m],['n','N',n],['o','O',o],['p','P',p],['q','Q',q],['r','R',r],['s','S',s],['t','T',t],['u','U',u],['v','V',v],['w','W',w],['x','X',x],['y','Y',y],['z','Z',z]]
realStat1 = [['a','A',8.2],['b','B',1.5],['c','C',2.8],['d','D',4.2],['e','E',12.7],['f','F',2.2],['g','G',2.0],['h','H',6.1],['i','I',7.0],['j','J',0.1],['k','K',0.8],['l','L',4.0],['m','M',2.4],['n','N',6.7],['o','O',7.5],['p','P',1.9],['q','Q',0.1],['r','R',6.0],['s','S',6.3],['t','T',9.0],['u','U',2.8],['v','V',1.0],['w','W',2.4],['x','X',2.0],['y','Y',0.1],['z','Z',0.1]]
realStat2 = [['a','A',8.34],['b','B',1.54],['c','C',2.73],['d','D',4.14],['e','E',12.6],['f','F',2.03],['g','G',1.92],['h','H',6.11],['i','I',6.71],['j','J',0.23],['k','K',0.87],['l','L',4.24],['m','M',2.53],['n','N',6.8],['o','O',7.7],['p','P',1.66],['q','Q',0.09],['r','R',5.68],['s','S',6.11],['t','T',9.37],['u','U',2.85],['v','V',1.06],['w','W',2.34],['x','X',0.2],['y','Y',2.04],['z','Z',0.06]]

#sort stats
def getKey(data):
    return data[2]
sampleStat.sort(key=getKey,reverse=True)
realStat1.sort(key=getKey,reverse=True)
realStat2.sort(key=getKey,reverse=True)

#find sample stat
SUM = 0
for sample in sampleStat:
    SUM += sample[2]
for sample in sampleStat:
    sample[2] = sample[2]*100/SUM

def lineDecoding(cipherText, realStat):
    decryptText = [' ' for I in cipherText]
    for I in range(len(cipherText)):
    #for I in range(len(cipherText)):
        foundMessage = False
        for J in range(26):
            if cipherText[I] == sampleStat[J][0]:
                decryptText[I] = realStat[J][0]
                foundMessage = True
                break
            elif cipherText[I] == sampleStat[J][1]:
                decryptText[I] = realStat[J][1]
                foundMessage = True
                break
        if not foundMessage:
            decryptText[I] = cipherText[I]
    return decryptText

def printStat(stat):
    print(stat[0], end=' ')
    if stat[2] / 10 < 1:
        print(" " + "{0:.2f}".format(stat[2]) + '%', end=' ')
    else:
        print("{0:.2f}".format(stat[2]) + '%', end=' ')

def printStatFull():
    print('')
    print('sample     real1      real2              sample     real1      real2')
    for I in range(13):
        printStat(sampleStat[I])
        print('  ', end='')
        printStat(realStat1[I])
        print('  ', end='')
        printStat(realStat2[I])
        
        print('          ', end='')

        printStat(sampleStat[I+13])
        print('  ', end='')
        printStat(realStat1[I+13])
        print('  ', end='')
        printStat(realStat2[I+13])
        print('')
    print('')

def printFullData():
    print("-----------------------------------------------------------------------------\nCipher Text")
    printText(cipherText)
    print("\nDecrypt Text 1")
    printText(lineDecoding(cipherText, realStat1))
    print("\nDecrypt Text 2")
    printText(lineDecoding(cipherText, realStat2))
    printStatFull()

printFullData()

def swap(A, B, realStat):
    if A == B:
        return
    for I in range(26):
        if A == realStat[I][0] or A == realStat[I][1]:
            TMP1 = I
            realStat[I][0] = B
            realStat[I][1] = B
            break
    for I in range(26):
        if (B == realStat[I][0] or B == realStat[I][1]) and I != TMP1:
            TMP2 = I
            realStat[I][0] = A
            realStat[I][1] = A
            break
    TMP3 = realStat[TMP1][2]
    realStat[TMP1][2] = realStat[TMP2][2]
    realStat[TMP2][2] = TMP3

def findIndex(char, stat):
    result = -1
    for I in range(len(stat)):
        if char == stat[I][0] or char == stat[I][1]:
            result = I
    return result

def setStat(KEY, realStat):
    swap(KEY[1], KEY[3], realStat)


KEY = input()
while 1:
    if KEY[0] == 'q' or KEY[0] == 'Q':
        break
    elif KEY[0] == '1':
        setStat(KEY, realStat1)
        swap(realStat2[findIndex(KEY[3], realStat1)][0], KEY[3],realStat2)
    elif KEY[0] == '2':
        setStat(KEY, realStat2)
        swap(realStat1[findIndex(KEY[3], realStat2)][0], KEY[3],realStat1)
    printFullData()
    KEY = input()
