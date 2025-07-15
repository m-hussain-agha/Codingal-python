lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Lenght of list", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Reveresed List :", lst)

print("Multiplication on list :", lst*2)

lst = lst[:4]
print("Sliced List :", lst)

lst.clear()
print("Updated List :", lst)