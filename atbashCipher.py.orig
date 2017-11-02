#Pyhton program to implement Atbash Cipher

#Its one of the simplest ciphers with almost no security

'''
Every character is reversed i.e. 'A' changes to 'Z'
and vice versa.
*-----------------------------------------------------*
* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z *
* | | | | | | | | | | | | | | | | | | | | | | | | | | *
* | | | | | | | | | | | | | | | | | | | | | | | | | | *
* V V V V V V V V V V V V V V V V V V V V V V V V V V *
* Z Y X W V U T S R Q P O N M L K J I H G F E D C B A *
*-----------------------------------------------------*
It can be thought of as an affine cipher
with a = 25 = b

'''
#This script uses dictionaries to lookup various alphabets
lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

'''
Since we are using a dictionary we don't need
separate functions for encryption and decryption
'''
def atbash(message):
    cipher = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            #adds the corresponding letter from the lookup_table
            cipher += lookup_table[letter]
        else:
            # adds space
            cipher += ' '

    return cipher

# Hard-coded driver function to run the program
def main():
    message = 'ALICE KILLED BOB'
    print(atbash(message.upper()))

    message = 'ZORXV PROOVW YLY'
    print(atbash(message.upper()))


#Executes the main function
if __name__ == '__main__':
    main()
