import sys
args = sys.argv[1:]

# 0 = key is valid, 1 = key isn't string
def keyValid(key):
    try:
        key = str(key)
    except ValueError:
        return 1
    return 0

def printError(typeOfError):
    print('Error: ', end='')
    if typeOfError == 1:
        print('key must be string')

def checkAlphabet(char):
    if ord(char) >= ord('a') and ord(char) <= ord('z'):
        return 'lower'
    elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return 'upper'
    return 'none'

def encryptMessage(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        x = ord(plaintext[i])
        TYPE = checkAlphabet(plaintext[i])
        if TYPE != 'none':
            if TYPE == 'lower':
                shift = ord('a')
            elif TYPE == 'upper':
                shift = ord('A')
            ciphertext += chr((x - shift + ord(key[i%len(key)]) - shift) % 26 + shift)
        else:
            ciphertext += plaintext[i]
    return ciphertext

def decryptMessage(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        y = ord(ciphertext[i])
        TYPE = checkAlphabet(ciphertext[i])
        if TYPE != 'none':
            if TYPE == 'lower':
                shift = ord('a')
            elif TYPE == 'upper':
                shift = ord('A')
            plaintext += chr((y - shift - (ord(key[i%len(key)]) - shift)) % 26 + shift)
        else:
            plaintext += ciphertext[i]
    return plaintext

def encryptWhenKeyIsValid(plaintext, key, silentMode):
    if keyValid(key) == 0:
        if not silentMode:
            print('Ciphertext: ', end='')
        print(encryptMessage(plaintext, key))
    else:
        printError(keyValid(key))

def decryptWhenKeyIsValid(ciphertext, key, silentMode):
    if keyValid(key) == 0:
        if not silentMode:
            print('Plaintext: ', end='')
        print(decryptMessage(ciphertext, key))
    else:
        printError(keyValid(key))

def encryptProgram():
    plaintext = input('Plaintext: ')
    key = input('Key: ')
    print('')
    encryptWhenKeyIsValid(plaintext, key, False)

def decryptProgram():
    ciphertext = input('Ciphertext: ')
    key = input('Key: ')
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

def twoArgsProgram(plaintext, key):
    encryptWhenKeyIsValid(plaintext, key, True)

def threeArgsProgram(text, key, mode):
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
elif len(args) == 2:
    plaintext = args[0]
    key = args[1]
    twoArgsProgram(plaintext, key)
elif len(args) == 3:
    text = args[0]
    key = args[1]
    mode = args[2]
    threeArgsProgram(text, key, mode)
