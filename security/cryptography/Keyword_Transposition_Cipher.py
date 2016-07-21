# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

num = int(raw_input())
for i in range(num):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    password = list(raw_input())
    message = raw_input()
    #remove duplicate letters in password and reverse
    k=len(password)
    for r in range(k-1,0,-1):
        if password.index(password[r]) < r:
           del password[r]
    password.reverse()


    #Create key
    for letter in password:
        key.remove(letter)
        key.insert(0,letter)

    #Create key block
    block = []
    for j in range(len(password)):
        block.append([])
    for letter in key:
        block[key.index(letter)%len(password)].append(letter)
    block.sort()
    for j in range(1,len(block)):
        for k in range(0,len(block[j])):
            block[0].append(block[j][k])

    decode = ""
    for letter in message:
        if letter == " ":
            decode = decode + " "
        else:
            decode = decode+alpha[block[0].index(letter)]
    print decode
