import time

fruits = ["apple", "banana", "orange", "mango", "cherry"]
quants = [10, 20, 8, 15, 12]

start_noob = time.perf_counter()
# noob
print('Noob:')
for i in range(len(fruits)):
    fv = fruits[i]
    qv = quants[i]
    print(i, fv, qv)
end_noob = time.perf_counter()


start_pro = time.perf_counter()
# Pro
print('\nPro: ')
for i, (fv, qv) in enumerate(zip(fruits, quants)):
    print(i, fv, qv)

end_pro = time.perf_counter()

print("Noob: ", end_noob - start_noob)
print("Pro:  ", end_pro - start_pro)
