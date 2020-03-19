""" 1.Выведите на печать вторую букву l из строки 'Hello Python!'
Присвойте строку переменной, затем выведите на печать букву"""

greeting = "Hello! Python"
print(greeting[3])

""" 2.Выведите на печать вторую букву l из строки 'Hello Python!'
Сделайте это без присваивания строки переменной, в одной
 строке кода. Если не знаете, как это сделать, попробуйте погуглить"""

print("Hello! Python"[3])

""" 3.Выведите на печать 'He' из строки 'Hello Python!' 
минимум двумя способами"""

print(greeting[0:2])
print(greeting[:2])
print(greeting[-13: -11])
print(greeting[-13: -11:1])
print(greeting[0:2:1])
print(greeting[:2:1])