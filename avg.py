n1=float(input("Enter n1: "))
n2=float(input("Enter n2: "))
n3=float(input("Enter n3: "))
n4=float(input("Enter n4: "))
n5=float(input("Enter n5: "))
avg=n1+n2+n3+n4+n5/5
if 401<=avg<=500:
    grade="A"
elif 301<=avg<=400:
    grade="B"
elif 201<=avg<=300:
    grade="C"
elif 101<=avg<=200:
    grade="D"
elif 91<=avg<=100:
    grade="E"
else:
    grade="F"
print("Grade is : ",grade)