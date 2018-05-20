def encrypt(clearText, key):
    result = ""
    matrix = [["" for x in range(len(clearText))] for y in range(key)]
    increment = 1
    row = 0
    col = 0
    for c in clearText:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1
        matrix[row][col] = c
        row += increment
        col += 1
    for mlist in matrix:
        result += "".join(mlist)
    return result


def decrypt(cipherText, key):
    result = ""
    matrix = [["" for x in range(len(cipherText))] for y in range(key)]
    idx = 0
    increment = 1
    for selectedRow in range(0, len(matrix)):
        row = 0
        for col in range(0, len(matrix[row])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            if row == selectedRow:
                matrix[row][col] += cipherText[idx]
                idx += 1
            row += increment
    matrix = transpose(matrix)
    for klist in matrix:
        result += "".join(klist)
    return result


def transpose(m):
    result = [[0 for y in range(len(m))] for x in range(len(m[0]))]
    for i in enumerate(m):
        for j in enumerate(m[0]):
            result[j][i] = m[i][j]
    return result


def main():
    clearText = "i am the king"
    print("Original Text: " + clearText)
    key = 3
    cipherText = encrypt(clearText, key)
    print("Encrypted Text: {0}".format(cipherText))
    decipherText = decrypt(cipherText, key)
    print("Decrypted Text: {0}".format(decipherText))
    return


if __name__ == '__main__':
    main()
