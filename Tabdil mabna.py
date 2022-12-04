def CharToNum(x):
    if x=="A":
        a=10
    elif x=="B":
        a=11
    elif x=="C":
        a=12
    elif x=="D":
        a=13
    elif x=="E":
        a=14
    elif x=="F":
        a=15
    return a

def NumToChar(x):
    if x==10:
        a="A"
    elif x==11:
        a="B"
    elif x==12:
        a="C"
    elif x==13:
        a="D"
    elif x==14:
        a="E"
    elif x==15:
        a="F"
    return a    

def ConvertAto10(n,a):
    t=len(n)
    golabi=0
    for i in range(0,t,1):
        if n[i].isdigit():
            aa=int(n[i])*a**(t-1-i)
            golabi+=aa
        else:
            s=CharToNum(n[i])
            bb=s*a**(t-1-i)
            golabi+=bb
    return(int(golabi))

def Convert10toA(n,a):
    golabi=""
    m = int(n)
    while m>a:
        s=m%a
        if m%a<10:
            golabi=golabi+str(s)
        else:
            p=NumToChar(s)
            golabi=golabi+p
        m=int(m/a)
    golabi+=str(m)
    sib=""
    for i in range(len(golabi)-1,-1,-1):
        sib=sib+golabi[i]
    return(sib)

def ConvertAtoB(n,a,b):
    x = ConvertAto10(n, a)
    golabi = Convert10toA(x, b)
    return (golabi)

print("Hi! Welcome to SB Base Convertor")
print()
n = str(input("Please Enter the Number: "))
a = int(input("Please Enter the Number's base: "))
if a<2 or a>16:
    print("The base must be in [2,16]")
    exit()
b = int(input("Please Enter the new base: "))
if b<2 or b>16:
    print("The base must be in [2,16]")
    exit()
print()
if b == 10:
    print(f"the new number is: {ConvertAto10(n,a)}")
elif a == 10:
    print(f"the new number is: {Convert10toA(n,b)}")
else:
    print(f"the new number is: {ConvertAtoB(n,a,b)}")