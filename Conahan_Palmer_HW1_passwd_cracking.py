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
wordListHashes = open("wordListHashes.txt", "w+")

def hashWords(inFile,outFile):
    for word in inFile:
        sha = hashlib.sha256()
        sha.update(word.encode())
        outFile.write(sha.hexdigest() + "\n")

def main():
    hashWords(wordList,wordListHashes)

main()

passwordHashes.close()
wordList.close()
wordListHashes.close()
