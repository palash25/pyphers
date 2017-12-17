def hill(code):
    decryptionKey = [[2, 0, 3],
                     [23, 5, 11],
                     [7, 6, 25]]
    code = code.lower()
    output = [[0], [0], [0]]
    counter = 0
    for character in code:
        number = ord(character) - 97
        output[counter][0] = number
        counter += 1

    result = [[0],
              [0],
              [0]]

    for i in range(len(decryptionKey)):
                for j in range(len(output[0])):
                    for k in range(len(output)):
                        result[i][0] += decryptionKey[i][k] * output[k][j]

    unCiphered = ""
    for r in result:
                numeric_letter = r[0] % 26
                val = chr(numeric_letter + 97)
                unCiphered = unCiphered + val

    return unCiphered


def main():
    code = raw_input("Enter ciphertext: ")
    print
    plaintext = ""

    while(code):
        ciphertext = code[:3]
        code = code[3:]
        plaintext = plaintext + hill(ciphertext)
        print plaintext
        print
    main()
