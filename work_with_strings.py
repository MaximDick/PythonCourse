"""
task1.
1.Создайте переменные, поместите в них значения - имя, фамилию
 и возраст. Выведите на экран следующее предложение:
 "Hi! My name is имя фамилия, I'm возраст years old."
 Используйте конкатенацию переменных и строк."""

name = str(input("name:\t"))
surname = str(input("surname:\t"))
years = str(input("years\t"))

print("Hi! My name is " + name + " " + surname + ", I'm " + years + " years old.")

"""
task2.
Выведите на экран текст детской песенки:
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full

One for the master,
One for the dame,
And one for the little boy
Who lives down the lane

Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full

Отступите от левого края расстояние, равное двум табуляциям. Выполните перенос текста на новую строку двумя способами
"""

print("\t\tBaa, baa, black sheep,\n \r\t\tHave you any wool?\n \r\t\tYes sir, yes sir,\n \r\t\tThree bags full\n")



print("""\n\t\tOne for the master,
\t\tOne for the dame,
\t\tAnd one for the little boy
\t\tWho lives down the lane

\t\tBaa, baa, black sheep,
\t\tHave you any wool?
\t\tYes sir, yes sir,
\t\tThree bags full""")

