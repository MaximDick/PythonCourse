# 1.Создайте переменные, поместите в них значения - имя,
# фамилию и возраст. Выведите на экран следующее предложение:
# "Hi! My name is имя фамилия, I'm возраст years old."
# Используйте конкатенацию переменных и строк.
first_name = "Ivan"
last_name = "Ivanov"
my_years = 25
print("Hi! My name is " + first_name + " " \
      + last_name + ", I'm " + str(my_years) + " years old.")

"""
2. Выведите на экран текст детской песенки:

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
Three bags full"""

# Отступите от левого края расстояние, равное двум табуляциям.
# Выполните перенос текста на новую строку двумя способами

print("\t\tBaa, baa, black sheep,\n\t\tHave you any wool?\n\t\tYes sir, yes sir,\n\t\tThree bags full\n")

print("""\t\tOne for the master,
\t\tOne for the dame,
\t\tAnd one for the little boy
\t\tWho lives down the lane\n
\t\tBaa, baa, black sheep,
\t\tHave you any wool?
\t\tYes sir, yes sir, 
\t\tThree bags full""")