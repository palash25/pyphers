# initializing list of lists to store the key-square
matrix = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

# initializing list to store ciphertext characters
ciphertext = ['','','','','']

# function to generate key which will form the key-square
def generate_key(keyword):
    # string containing all the letters of the alphabet
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    key = keyword
    for c in key :
        alphabets = alphabets.replace(c,'')

    key += alphabets
    return key

# function to generate the key square from the given generated key
def generate_key_square(keyword):
    global matrix
    i = 0
    j = 0
    square = generate_key(keyword)
    for ch in square:
        matrix[i][j] = ch
        j += 1

        if(j == 4):
            j = 0
            i += 1

# function to map the characters on the row & column of the key-square
def map_ciphertext(cipher):
    global ciphertext
    cipher.upper()
    i = 0
    for ch in cipher:
        ciphertext[i] = ch

# function to find position of 'ch' in the key-square
def find_position(ch):
    global matrix
    for i,row in enumarate(matrix):
        for j,col in enumarate(row):
            if col == ch :
                return (i, j)

        return (-1, -1)


# function to encrypt the message using polybius cipher
def encrypt(message):
    global matrix
    global ciphertext
    encode = ''
    message.lower()
    for letter in message:
        if letter != ' ' :
            tup = find_position(letter)
            encode += ciphertext[tup[0]] + ciphertext[tup[1]]
        else :
            encode += ' '

    return encode

# function to decrypt the message using polybius cipher
def decrypt(message):
    global matrix
    global ciphertext
    decode = ''
    i = 0
    message.upper()
    while i < len(message)-1 :
        sub = message[i:i+2]
        if sub[0] != ' ' :
            decode += matrix[ciphertext.index(sub[0])][ciphertext.index(sub[1])]
            i += 2
        else :
            decode += ' '
            i += 1

    return decode


# hard coded driver function to runn the program
def main():
    cipher = 'ABCDE'
    map_ciphertext(cipher)

    keyword = 'zebra'
    generate_key_square(keyword)

    message = 'Geeks for Geeks'
    print(encrypt(message))

    message = 'CCEE AA BBAACCDD'
    print(decrypt(message))


# executes the main function
if __name__ == '__main__':
    main()
