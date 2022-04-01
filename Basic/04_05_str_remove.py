##########################################
# This code is created by Hesam Marshal  #
# Website : Chaptera.ir                  #
# instagram: @HesamMarshal               #
# Remove characters from a string        #
##########################################
str = input("Enter your string: ")

final_str = ""

for character in str:
    if character != 'a' and character != 'e' and character != 'i' and character != 'u' and character != 'o':
        final_str += character
print(final_str)
