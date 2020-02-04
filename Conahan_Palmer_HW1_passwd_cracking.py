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

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import hashlib

passwordHashes = open("hashes.txt", "r")

crackedPasses = open("crackedPasses.txt", "w")

def hashWord(word):
    convertWord = word.split()
    sha = hashlib.sha256()
    sha.update(convertWord[0].encode())
    return sha.hexdigest()

def retHash(pwLine):
    splitLine = pwLine.split(":")
    return splitLine[1]

def ruleOne(passHashes):
    pwFound = bool(0)
    wordList = open("words", "r")
    print("Attempting to crack using rule one")

    while(not pwFound):
        line = wordList.readline()
       
        if len(line) == 8:
            capAppendBool = bool(0)
            capAppend = line.capitalize()
            num = 0
           
            while(num <= 9):                
                capAppendNum = capAppend.strip() + str(num)
                #print(capAppendNum)
                num = num + 1
                passHashes.seek(0)
               
                for passHashLine in passHashes:
                    #print("Comparing " + capAppendNum + ": " + hashWord(capAppendNum) + " with " + retHash(passHashLine))
                    if hashWord(capAppendNum) == retHash(passHashLine):
                        print("Cracked Password: " + capAppendNum)
                        pwFound = bool(1)
                        num = 10
        elif not line:
            pwFound = bool(1)
            wordList.close()

def ruleFive(passHashes):
    pwFound = bool(0)
    wordList = open("words.txt", "r")
    print("Attempting to crack using rule five")
    
    while(not pwFound):
        line = wordList.readline()
        stripLine = line.strip()
        passHashes.seek(0)

        for passHashLine in passHashes:
            #print("Comparing " + stripLine + ": " + hashWord(stripLine) + " with " + retHash(passHashLine))
            if hashWord(stripLine) == retHash(passHashLine):
                print("Cracked Password: " + stripLine)
                pwFound = bool(1)
                wordList.close()

def main():
    ruleOne(passwordHashes)
    ruleFive(passwordHashes)

main()
passwordHashes.close()
crackedPasses.close()
