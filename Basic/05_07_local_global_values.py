
##########################################
# This code is created by Hesam Marshal  #
# Website : Chaptera.ir                  #
# instagram: @HesamMarshal               #
# Local nd global Values                 #
##########################################
lastname = "Akrami"


def my_func(name):
    global lastname
    lastname = "Marshal"


print(lastname)
my_func("Hesam")
print(lastname)
