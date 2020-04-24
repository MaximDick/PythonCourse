"""1.Используйте цикл for для вычисления суммы всех чётных чисел в
 диапазоне от 10 до 30 (включая крайние значения).
Выведите результат на печать"""

summa = 0
for number in range(10, 31):
    if number % 2 == 0:
        summa += number
print(summa)

"""2.Получите от пользователя число на вводе и используйте цикл for
 для вывода на экран текста 'Hello!' столько же раз"""
value = int(input('Enter number: '))
for _ in range(value):
    print('Hello')