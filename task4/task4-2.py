#Напишите программу для проверки длины введенного пароля с использованием цикла while.
#Программа должна запрашивать у пользователя ввод пароля и проверять его длину.
#Длина пароля должна быть не менее 8 символов.

password = input("Введите желаемый пароль: ")
while len(password) < 8:
    print("Пароль должен быть больше 8 символов")
    password = input("Введите желаемый пароль: ")

print(f"Вы ввели хороший пароль {password}")