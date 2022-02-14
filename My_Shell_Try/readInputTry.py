#! /usr/bin/python3
import os,sys,re

input = os.read(0,100).decode()

print(input)



input = input.replace("\n","")
input = re.split(' ',input)

print(input)
