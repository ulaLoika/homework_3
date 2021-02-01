# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    if a>b>c:
        d=a+b
        return(d)
    elif a>c>b:
        d=a+c
        return(d)
    elif b>a>c:
        d=b+a
        return(d)
    elif b>c>a:
        d=b+c
        return(d)
    elif c>b>a:
        d=c+b
        return(d)
    elif c>a>b:
        d=c+a
        return(d)


a,b,c = input('Введите три числа: ').split()
a = int(a)
b = int(b)
c = int(c)
print (f'Сумма двух наибольших чисел равна: {my_func(a,b,c)}')
