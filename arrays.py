# tupel st array aber unveränderbar
# array kann auch array beinhalten
# array = [2, True, "2222 ", [0,1]]
# # array kann auch unterschiedliche Datentypen tragen
# print(array)
# for i in range(len(array)):
#     array.append(i)
#     array[i] = array[i] * i
#     print(array[i])
#     print(array)

liste = []


for i in range(1,101):
    liste.append(i)

# for i in range(2,101,2):
#     liste.append(i)
for i in liste:
    if i % 2 == 0:
        print(i)