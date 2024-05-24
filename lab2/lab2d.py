#!/usr/bin/env python3
import sys
sys.argv[0]
if len(sys.argv) != 3:
    print('Usage: ./lab2d.py name age')
    sys.exit


#name = input("Name: " )
#age = input("Age: ")
#Does not equal 3 since it counts the name as the 1st parameter

else:
    name = sys.argv[1]
    age = sys.argv[2]
    print('Hi ' + name + ', you are ' + (age) + ' years old.')