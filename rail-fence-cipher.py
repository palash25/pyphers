
def main():
    # get the number of layers to rail encrypt
    layers = int(input("Enter the number of layers: "))

    # get the plain text
    plain_text = input("Enter the plain text: ")

    # encrypt the plain text
    cipher_text = encrypt(layers, plain_text)
    print("Encrypted text: " + cipher_text)


def encrypt(layers, plain_text):
    # remove all white spaces in text
    plain_text = plain_text.replace(" ", "")

    # change plain text to upper case
    plain_text = plain_text.upper()

    # divide plain text into layers number of strings
    rail = [""] * layers
    layer = 0
    for character in plain_text:
        rail[layer] += character
        if layer >= layers - 1:
            layer = 0
        else:
            layer += 1

    cipher = "".join(rail)
    return cipher


if __name__ == '__main__':
    main()
