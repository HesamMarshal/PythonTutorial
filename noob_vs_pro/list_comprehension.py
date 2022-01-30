fruits = [("apple", 10), ("banana", 20),
          ("orange", 30), ("kiwi", 14), ("mango", 8)]
shortage = []
# for x, q in fruits:
#     if q < 15:
#         shortage.append(x)

shortage = [(x, 15-q) for x, q in fruits if q < 15]
print(shortage)
