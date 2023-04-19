s = input("Enter numbers: ").split(" ")

dict = {}
for el in s:
    if el in dict:
        print(f"{el}_{dict[el]}", end=' ')
        dict[el] = dict[el]+1
    else:
        print(el, end=' ')
        dict[el] = 1
