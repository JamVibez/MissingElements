print("Wprowadź rozmiar tablicy do porównania")
listsize = int(input())
elements_in_list = [2, 3, 7, 4, 9]
new_list = []
for x in range (1,listsize+1):
    new_list.append(x)

print(list(set(new_list).difference(set(elements_in_list))))