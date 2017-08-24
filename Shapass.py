# By Dagito from 0xDev
import hashlib


def cryptopass(password):
    aplication = input("What app is this password for? ")
    for random in range(len(password)):
        sha = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print("Your new password is " + "".join(sha).replace(' ', ''))
    save = open("Password.txt", "a")
    save2 = open("Key Phrase.txt", "a")
    save2.write("Your key phrase for " + aplication + " was " + password)
    save2.write("\n")
    save.write("Your new password for " + aplication + " is " + " " +
               "".join(sha).replace(' ', ''))
    save.write("\n")
    save.close()


password = input("Type a key phrase ")
cryptopass(password)
