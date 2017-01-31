import math
a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=0

cipherText = input()

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

def printCipherText():
    for I in cipherText:
        print(I, end='')
    print('')

def getKey(data):
    return data[2]

sampleStat = [['a','A',a],['b','B',b],['c','C',c],['d','D',d],['e','E',e],['f','F',f],['g','G',g],['h','H',h],['i','I',i],['j','J',j],['k','K',k],['l','L',l],['m','M',m],['n','N',n],['o','O',o],['p','P',p],['q','Q',q],['r','R',r],['s','S',s],['t','T',t],['u','U',u],['v','V',v],['w','W',w],['x','X',x],['y','Y',y],['z','Z',z]]
realStat1 = [['a','A',8.2,'1'],['b','B',1.5,'1'],['c','C',2.8,'1'],['d','D',4.2,'1'],['e','E',12.7,'1'],['f','F',2.2,'1'],['g','G',2.0,'1'],['h','H',6.1,'1'],['i','I',7.0,'1'],['j','J',0.1,'1'],['k','K',0.8,'1'],['l','L',4.0,'1'],['m','M',2.4,'1'],['n','N',6.7,'1'],['o','O',7.5,'1'],['p','P',1.9,'1'],['q','Q',0.1,'1'],['r','R',6.0,'1'],['s','S',6.3,'1'],['t','T',9.0,'1'],['u','U',2.8,'1'],['v','V',1.0,'1'],['w','W',2.4,'1'],['x','X',2.0,'1'],['y','Y',0.1,'1'],['z','Z',0.1,'1']]
realStat2 = [['a','A',8.34,'1'],['b','B',1.54,'1'],['c','C',2.73,'1'],['d','D',4.14,'1'],['e','E',12.6,'1'],['f','F',2.03,'1'],['g','G',1.92,'1'],['h','H',6.11,'1'],['i','I',6.71,'1'],['j','J',0.23,'1'],['k','K',0.87,'1'],['l','L',4.24,'1'],['m','M',2.53,'1'],['n','N',6.8,'1'],['o','O',7.7,'1'],['p','P',1.66,'1'],['q','Q',0.09,'1'],['r','R',5.68,'1'],['s','S',6.11,'1'],['t','T',9.37,'1'],['u','U',2.85,'1'],['v','V',1.06,'1'],['w','W',2.34,'1'],['x','X',0.2,'1'],['y','Y',2.04,'1'],['z','Z',0.06,'1']]
sampleStat.sort(key=getKey,reverse=True)
realStat1.sort(key=getKey,reverse=True)
realStat2.sort(key=getKey,reverse=True)

SUM = 0
for sample in sampleStat:
    SUM += sample[2]
for sample in sampleStat:
    sample[2] = sample[2]*100/SUM

def lineDecoding(cipherText, sampleStat, realStat):
    print('')
    for I in range(len(cipherText)):
        letterNumber = -1
        isCapital = False
        for J in range(len(sampleStat)):
            if cipherText[I] == sampleStat[J][0]:
                letterNumber = J 
                break
            elif cipherText[I] == sampleStat[J][1]:
                letterNumber = J 
                isCapital = True
                break
        if letterNumber < 0:
            print(cipherText[I], end='')
        else:
            if isCapital:
                print(realStat[J][1], end='')
            else:
                print(realStat[J][0], end='')
    print('')

lineDecoding(cipherText, sampleStat, realStat1)
lineDecoding(cipherText, sampleStat, realStat2)

def printAlphabet(stat):
    print('')
    for X in stat:
        print(X[0], end='')
    print('')

def printStat():
    print('')
    for I in range(26):
        print(sampleStat[I][0], end=' ')
        print(sampleStat[I][2], end=' ')

        print(realStat1[I][0], end=' ')
        print(realStat1[I][2], end=' ')
        if realStat1[I][3] == '9':
            print('***', end=' ')
        elif realStat1[I][3] != '1':
            print('***' + realStat1[I][3] + '***', end=' ')

        print(realStat2[I][0], end=' ')
        print(realStat2[I][2], end=' ')
        if realStat2[I][3] == '9':
            print('***', end=' ')
        elif realStat2[I][3] != '1':
            print('***' + realStat2[I][3] + '***', end=' ')
        print('')
    print('')

printStat()
def setStat(KEY, realStat):
    KEY2 = ['1' for I in range(5)]
    for I in range(len(KEY)):
        KEY2[I] = KEY[I]

    for I in range(26):
        if KEY2[1] == realStat[I][0] or KEY2[1] == realStat[I][1]:
            if KEY2[4] == '3':
                realStat[I][3] = '9'
            elif realStat[I][3] == '1' or KEY2[4] == '2':
                realStat[I][3] = realStat[I][0]
                realStat[I][0] = KEY2[3]
                realStat[I][1] = KEY2[3]


KEY = input()
while 1:
    if KEY[0] == 'q' or KEY[0] == 'Q':
        break
    elif KEY[0] == '1':
        setStat(KEY, realStat1)
    elif KEY[0] == '2':
        setStat(KEY, realStat2)
    printCipherText()
    lineDecoding(cipherText, sampleStat, realStat1)
    lineDecoding(cipherText, sampleStat, realStat2)
    printStat()
    KEY = input()
