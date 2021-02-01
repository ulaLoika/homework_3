# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def polzovatel (name, surname, DOB, city, email, tel):
    return f'имя - {name}; фамилия - {surname}; год рождения - {DOB}; город проживания - {city}; email - {email}; телефон - {tel}'

name, surname, DOB, city, email, tel = input ('Введите: имя, фамилия, год рождения, город проживания, email, телефон - через пробел: ').split()
print (polzovatel(name = name, surname = surname, DOB = DOB, city = city, email = email, tel = tel))
