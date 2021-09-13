print('Введите число(Если система >10 вводите буквы на английском языке) - ')
a=input()
b=''
print('Через пробел введите систему, в которой находится число и система, в которую будет совершен перевод - ')
n,n1=[int(s) for s in input().split()]
if n==10:
    if n1<10:
        a=int(a)
        k=0
        newnum=0
        while a>0:
            ost=a%n1
            newnum=newnum+ost*(10**k)
            k+=1
            a=a//n1
    else:
        newnum=''
        a=int(a)
        while a>0:
            ost=a%n1
            if ost<10:
                b=str(ost)
                newnum+=b
            else:
                if ost==10:
                    newnum+='A'
                elif ost==11:
                    newnum+='B'
                elif ost==12:
                    newnum+='C'
                elif ost==13:
                    newnum+='E'
                elif ost==14:
                    newnum+='D'
                elif ost==15:
                    newnum+='F'
            a=a//n1
        newnum=newnum[::-1]
elif n<10:
    a=int(a)
    k=0
    newnum1=0
    while a>0:
        ost=a%10
        newnum1=newnum1+ost*(n**k)
        a=a//10
        k+=1
    if n1<10:
        newnum=0
        k=0
        while newnum1>0:
            ost=newnum1%n1
            newnum=newnum+ost*(10**k)
            k+=1
            newnum1=newnum1//n1
    else:
        newnum=''
        while newnum1>0:
            ost=newnum1%n1
            if ost<10:
                b=str(ost)
                newnum+=b
            else:
                if ost==10:
                    newnum+='A'
                elif ost==11:
                    newnum+='B'
                elif ost==12:
                    newnum+='C'
                elif ost==13:
                    newnum+='E'
                elif ost==14:
                    newnum+='D'
                elif ost==15:
                    newnum+='F'
            newnum1=newnum1//n1
        newnum=newnum[::-1]
elif n>10:
    newnum1=0
    for i in range(len(a)):
        if a[len(a)-i-1]=='A':
            newnum1=newnum1+10*(n**i)
        elif a[len(a)-i-1]=='B':
            newnum1 = newnum1 + 11*(n**i)
        elif a[len(a)-i-1]=='C':
            newnum1 = newnum1 + 12*(n**i)
        elif a[len(a)-i-1]=='D':
            newnum1 = newnum1 + 13*(n**i)
        elif a[len(a)-i-1]=='E':
            newnum1 = newnum1 + 14*(n**i)
        elif a[len(a)-i-1]=='F':
            newnum1 = newnum1 + 15*(n**i)
        else:
            b=int(a[len(a)-1-i])
            newnum1 = newnum1 + b*(n**i)
    if n1<10:
        newnum=0
        k=0
        while newnum1>0:
            ost=newnum1%n1
            newnum=newnum+ost*(10**k)
            k+=1
            newnum1=newnum1//n1
    else:
        newnum=''
        while newnum1>0:
            ost=newnum1%n1
            if ost<10:
                b=str(ost)
                newnum+=b
            else:
                if ost==10:
                    newnum+='A'
                elif ost==11:
                    newnum+='B'
                elif ost==12:
                    newnum+='C'
                elif ost==13:
                    newnum+='E'
                elif ost==14:
                    newnum+='D'
                elif ost==15:
                    newnum+='F'
            newnum1=newnum1//n1
        newnum=newnum[::-1]
print(newnum)
