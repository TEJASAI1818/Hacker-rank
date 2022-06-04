
x = input("enter filename : ")

len = len(x)
s = 0

for i in range(len) :
    if x[i] == '.' :
        s = i
        break
else :
    print("enter extension also")

ex = ""

for j in range(s+1,len) :
    ex += x[j]

if ex == 'py' :
    print("The extension of the file is : 'python'")
elif ex == 'java' :
    print("The extension of the file is : 'java'")
elif ex == 'js' :
    print("The extension of the file is : 'java script'")
elif ex == 'cp' :
    print("The extension of the file is : 'c++'")
elif ex == 'txt' :
    print("The extension of the file is : 'Text'")
elif ex == 'c' :
    print("The extension of the file is : 'C'")
elif ex == 'html' :
    print("The extension of the file is : 'HTML'")
else :
    print("Invalid Extension")
