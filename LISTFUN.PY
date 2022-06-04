lst = []
x = int(input("enter no of elements in a list : "))
for i in range(0, x):
    y = int(input("enter the element : "))
    lst.append(y)
for i in lst:
    if i < 0:
        lst.remove(i)
print(lst)
