##########################################
# This code is created by Hesam Marshal  #
# Website : Chaptera.ir                  #
# instagram: @HesamMarshal               #
# List: Add remove items                 #
##########################################

letters = ["a", "b", "c"]
# print("before append: ", letters)
letters.append("d")
letters.append("e")
# print("after append: ", letters)


# print("before insert: ", letters)
# # letters.insert(0, "0")
# letters.insert(1, "x")

# print("before pop: ", letters)
# x = letters.pop(1)
# print("after pop: ", letters)
# print(x)

# print("before remove: ", letters)
# letters.remove("b")
# print("after remove: ", letters)


print("before del: ", letters)
del(letters[1:3])
print("after del: ", letters)
