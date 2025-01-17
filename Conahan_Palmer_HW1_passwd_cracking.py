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

crackedPasses = open("crackedPasses.txt", "w")


def ruleFive(passHashes):
    print("Attempting to crack using rule five")
    for line in passHashes:
        splitLine = line.split(":")
        passHash = splitLine[1]
        wordList = open("words.txt", "r") #"/usr/share/dict/words"
        for wordLine in wordList:
            word = wordLine.split()
            sha = hashlib.sha256()
            sha.update(word[0].encode())
            if sha.hexdigest() == passHash:
                print ("Cracked Password: " + word[0])
                crackedPasses.write("encrypted:" + word[0])
                break
        wordList.close()
            
                
def main():
    ruleFive(passwordHashes)
    

main()

passwordHashes.close()
crackedPasses.close()
