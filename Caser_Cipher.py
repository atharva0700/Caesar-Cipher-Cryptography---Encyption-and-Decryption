# TOOL:  Cryptool

#substitution

#1.) Caeser cipher

print("==================================================================")
print("")
print("                     C R Y P T O G R A P H Y                      ")
print("")
print("==================================================================")
print("")
print(" a b c d e f g h i j  k  l  m  n  o  p   q  r  s  t  u  v  w  x  y  z")
print(" 0 1 2 3 4 5 6 7 8 9 10  11 12 13 14 15 16 17 18 19 20 21 22 23 24 25")
print("")
print("==================================================================")
print(" ---------------Welcome In CryptoGraphy world-------------------  ")
print("")
print(" ---------------------1.) Caser Cipher -------------------------  ")
print("A: Encrypt your text using Caser method")
print("B: Decrypt your Caser Encrypted text")
option = raw_input("Choose your option? (A/B)")
s = ""
encrypt_list = []
decrypt_list = []
try:
	if(option == 'A' or option == 'a'):
		print("----------------Welcome In Encryption world--------------")
		plain_text = raw_input("Enter Plain-text/Original-text here:")
		key = int(raw_input("Enter Encryption key here: "))
		for i in plain_text:
			x = ord(i) + key
			encrypt_list.append(chr(x))
		x_str = ''.join(encrypt_list)
		print(x_str)

	elif(option == 'B' or option == 'b'):
		cipher_text = raw_input("Enter cipher-text/encrypted-text here:")
		key = int(raw_input("Enter Decryption key here: "))
		for i in cipher_text:
			x = ord(i) - key
			decrypt_list.append(chr(x))
		
		y_str = ''.join(decrypt_list)
		print(y_str)

except Exception as e:
	print("Something is wrong here, please start again from begining.")