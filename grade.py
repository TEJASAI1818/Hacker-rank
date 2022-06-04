print("1. 2nd year sem 2\n"
      "2. 3rd year sem 1\n"
      "3. 3rd year sem 2\n"
      "4. 4th year sem 1\n"
      "5. 4th year sem 2")

def cgpa(subjects,credits) :
    grades = []
    tcg = []

    for i in range(len(credits)):
        x = int(input("enter your grade : "))
        grades.append(x)
        tcg.append(credits[i] * grades[i])

    totg = sum(tcg)
    tc = sum(credits)
    print("Your grades are : ")
    data = dict(zip(subjects,grades))
    print(data)
    return totg/tc

def year22():
    subjects = ['CO', 'OS', 'DBMS', 'FLAT', 'IIM', 'IOR']
    credits = [3, 3, 3, 3, 3, 3]

    result = cgpa(subjects,credits)
    print("your cgpa for 2nd year SEM_2 is ", result)

def year31():
    subjects = ['CN','DAA','WT','SE','PE1','OE2','DAA_LAB','WT_LAB','SE_LAB']
    credits = [3,3,3,3,3,3,2,2,2]

    result = cgpa(subjects,credits)
    print("Your 3rd year sem 1 result is : ",result  )

def year32():
    subjects = ['CD', 'DE', 'AI', 'CNS', 'PE2', 'OE3', 'AI_LAB', 'PROJECT1', 'TERM_PAPER']
    credits = [3, 3, 3, 3, 3, 3, 2, 2, 2]

    result = cgpa(subjects, credits)
    print("Your 3rd year sem 2 result is : ", result)

def year41():
    subjects = ['MACHINE LEARNING','NEURAL NETWORKS','PE3','PE4','HUMANITIES','ML LAB','PROJECT2']
    credits = [3,3,3,3,3,1,2]

    result = cgpa(subjects, credits)
    print("Your 4th year sem 1 result is : ", result)

def year42():
    subjects = ['PE5','OE4','PROJECT3']
    credits = [3,3,6]

    result = cgpa(subjects, credits)
    print("Your 4th year sem 1 result is : ", result)

while True:
    x = int(input('enter the option '))
    if x == 0 or x > 5:
        print("invalid number")

    elif x == 1:
        year22()
        break

    elif x == 2:
        year31()
        break

    elif x == 3:
        year32()
        break

    elif x == 4:
        year41()
        break

    elif x == 5:
        year42()
        break