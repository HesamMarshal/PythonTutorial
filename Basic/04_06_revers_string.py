##########################################
# This code is created by Hesam Marshal  #
# Website : Chaptera.ir                  #
# instagram: @HesamMarshal               #
# Reverse the String                     #
##########################################
'''
Sara
araS
'''

from numpy import outer


mystr = "Sara"
outstr = ""

for char in mystr:
    outstr = char + outstr

print(outstr)


outstr2 = ""

i = 0
while i < len(mystr):
    outstr2 = mystr[i] + outstr2
    i += 1

print(outstr2)
