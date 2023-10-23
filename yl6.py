a = input("Sisesta arv 1: ")
b = input("Sisesta arv 2: ")
c = input("Sisesta arv 3: ")
if int(a) > int(b) and int(a) > int(c): 
    print(a)
elif  int(b) > int(c):
    print(b)
else:
    print(c)