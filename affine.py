import sys
args = sys.argv[1:]

def gcd(x, y):
    MIN = min(x, y) 
    MAX = max(x, y)
    i = MIN
    while i > 0:
        if (MIN % i) == 0 and (MAX % i) == 0:
            return i
        i -= 1

def modInverse(x, mod):
    if gcd(x, mod) == 1:
        for i in range(mod):
            if (x * i) % mod == 1:
                return i
    return 0

# 0 = key is valid, 1 = key isn't int, 2 = can't find modInverse for the first key
def keyValid(key):
    try:
        key[0] = int(key[0])
        key[1] = int(key[1])
    except ValueError:
        return 1
    except IndexError:
        return 2
    if key[0] % 2 == 0 or key[0] % 13 == 0:
        return 3
    return 0

def printError(typeOfError):
    print('Error: ', end='')
    if typeOfError == 1:
        print('key must be integer')
    elif typeOfError == 2:
        print('key must be 2 integers, such as 3 10 or 21 9')
    elif typeOfError == 3:
        print('the first key must be in this set {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}')

def checkAlphabet(char):
    if ord(char) >= ord('a') and ord(char) <= ord('z'):
        return 'lower'
    elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return 'upper'
    return 'none'

def encryptMessage(plaintext, key):
    ciphertext = ''
    for T in plaintext:
        x = ord(T)
        TYPE = checkAlphabet(T)
        if TYPE != 'none':
            if TYPE == 'lower':
                shift = ord('a')
            elif TYPE == 'upper':
                shift = ord('A')
            ciphertext += chr(((x - shift) * int(key[0]) + int(key[1])) % 26 + shift)
        else:
            ciphertext += T
    return ciphertext

def decryptMessage(ciphertext, key):
    plaintext = ''
    for T in ciphertext:
        y = ord(T)
        TYPE = checkAlphabet(T)
        if TYPE != 'none':
            if TYPE == 'lower':
                shift = ord('a')
            elif TYPE == 'upper':
                shift = ord('A')
            plaintext += chr(((y - shift - int(key[1])) * modInverse(int(key[0]), 26)) % 26 + shift)
        else:
            palintext += T
    return plaintext

def encryptWhenKeyIsValid(plaintext, key, silentMode):
    if keyValid(key) == 0:
        if not silentMode:
            print('Ciphertext: ')
        print(encryptMessage(plaintext, key))
    else:
        printError(keyValid(key))

def decryptWhenKeyIsValid(ciphertext, key, silentMode):
    if keyValid(key) == 0:
        if not silentMode:
            print('Plaintext: ')
        print(decryptMessage(ciphertext, key))
    else:
        printError(keyValid(key))

def encryptProgram():
    plaintext = input('Plaintext: ')
    key = input('Key: ').split(' ')
    print('')
    encryptWhenKeyIsValid(plaintext, key, False)

def decryptProgram():
    ciphertext = input('Ciphertext: ')
    key = input('Key: ').split(' ')
    print('')
    decryptWhenKeyIsValid(ciphertext, key, False)

def modeValid(mode):
    try:
        mode = int(mode)
    except ValueError:
        return 1
    if not (mode == 0 or mode == 1): 
        return 2
    return 0

def printModeError(typeOfError):
    print('Error: ', end='')
    if typeOfError == 1:
        print('mode must be integer')
    if typeOfError == 2:
        print('mode must be only 0 or 1 (0 = encryption mode, 1 = decryption mode)')

def oneArgsProgram(mode):
    if modeValid(mode) == 0:
        if int(mode) == 0:
            encryptProgram()
        elif int(mode) == 1:
            decryptProgram()
    else:
        printModeError(modeValid(mode))

def threeArgsProgram(plaintext, key):
    encryptWhenKeyIsValid(plaintext, key, True)

def fourArgsProgram(text, key, mode):
    if modeValid(mode) == 0:
        if int(mode) == 0:
            encryptWhenKeyIsValid(text, key, True)
        elif int(mode) == 1:
            decryptWhenKeyIsValid(text, key, True)
    else:
        printModeError(modeValid(mode))

if len(args) == 0:
    encryptProgram()
elif len(args) == 1:
    mode = args[0]
    oneArgsProgram(mode)
elif len(args) == 3:
    plaintext = args[0]
    key = [' ' for i in range(2)]
    key[0] = args[1]
    key[1] = args[2]
    threeArgsProgram(plaintext, key)
elif len(args) == 4:
    text = args[0]
    key = [' ' for i in range(2)]
    key[0] = args[1]
    key[1] = args[2]
    mode = args[3]
    fourArgsProgram(text, key, mode)
