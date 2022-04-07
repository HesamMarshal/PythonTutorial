##########################################
# This code is created by Hesam Marshal  #
# Website : Chaptera.ir                  #
# instagram: @HesamMarshal               #
# Nested While                           #
##########################################

# # Two Layers
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')

i = 1
while i < 10:
    j = 1
    while j < 10:
        print(f'{i} * {j} = {i*j}')
        j += 1
    i += 1
