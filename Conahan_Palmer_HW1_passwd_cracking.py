#Name: Cormac Conahan & Scott Palmer
#Filename:  Conahan_Palmer_HW1_passwd_cracking.py
#
#Problem: Create a password cracker which implements SHA-256 hashing and
#         some additional rules
#
#Input: A text file containing a wordlist of possible passwords,
#       a text file containing hashed passwords
#Output: A text file containing the cracked passwords
#
#Certification of Authenticity:
#   I certify that this program is entirely my and my partner's own work.

import hashlib


passwordHashes = open("hashes.txt", "r")

wordList = open("words.txt", "r") #"/usr/share/dict/words"

crackedPasses = open("crackedPasses.txt", "w")


def ruleFive(passHashes,words):
    print("Attempting to crack using rule five")
    for line in passHashes:
        splitLine = line.split(":")
        passHash = splitLine[1]
        for word in words:
            sha = hashlib.sha256()
            sha.update(word.encode())
            if sha.hexdigest() == passHash:
                print ("Cracked Password: " + word)
                crackedPasses.write("encrypted:" + word)
                break
            
                
def main():
    ruleFive(passwordHashes,wordList)
    

main()

passwordHashes.close()
wordList.close()
crackedPasses.close()
