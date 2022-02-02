import os, sys, time, re

pid = os.getpid()

os.write(1,("Welcome to Jurassic park>>>\n").encode())
while(1):
    userInput = input(">>")
    os.write(1,(userInput"\n").encode())
    
    
