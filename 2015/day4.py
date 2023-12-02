import hashlib

initKey = "iwrupvqb"
number = 0
while True:
	key = initKey + str(number)
	md5_hash = hashlib.md5()
	md5_hash.update(key.encode('utf-8'))
	md5_hex = md5_hash.hexdigest()

	print("Current Number: ", number, " Current MD5: ", md5_hex)
	if md5_hex[:6] == "000000":
		break
	number += 1
