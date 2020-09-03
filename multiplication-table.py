#############
#Module:    multiplication-table.py
#Author:    Me
#Version:   Draft
'''
This program provides a simple multiplication table of 2-12.
'''
#############
#Log
#09/03/2020  -File created
#
#############
print("Come, let's practice our multiplication tables!")

for multiplier in range(2,13):  
    print( "This is our %dx multiplication table: " % (multiplier) )  # here I used the % string operator to create a Python format string and the 'multiplier' variable
    for j in range(1,13):
        print( "%d x %d  = %d" % (j, multiplier, j*multiplier) )
    print( "That was our %dx multiplication table! " % (multiplier) )
