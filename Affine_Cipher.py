#Python program to illustrate Affine Cipher
#For explaination refer to GeeksforGeeks


# Dictionary to lookup the index of alphabets
dict1 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
         'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

dict2={0:'A',1:'B',2:'C',3:'D',4:'E',
       5:'F',6:'G',7:'H',8:'I',9:'J',
       10:'K',11:'L',12:'M',13:'N',14:'O',
       15:'P',16:'Q',17:'R',18:'S',19:'T',
       20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

#Key valus
a=17
b=20

#Funtion to encrypt message
def Encrypt(msg):
	cipher=''
	for letter in msg:
		if letter==' ':
			cipher+=' '
		else:
			z=(a*dict1[letter]+b)%26
			cipher+=dict2[z]

	return cipher

#Funtion to decrypt cipher
def Decrypt(cipher):
	message=''
	a_inv=0
	flag=0
	#Find a^-1, the multiplicative inverse of a in the group of integers modulo m.
	#Here m=26
	for i in range(26):
		flag=(a*i)%26
		if flag==1:
			a_inv=i
			break

	for letter in cipher:
		if letter==' ':
			message+=' '
		else:
			z=(a_inv*(dict1[letter]-b))%26
			message+=dict2[z]

	return message

#Main function
def main():
	msg="AFFINE CIPHER"

	cipherText=Encrypt(msg)
	print(cipherText)

	originalText=Decrypt(cipherText)
	print(originalText)

#Executes the main function
if __name__ == '__main__':
	main()