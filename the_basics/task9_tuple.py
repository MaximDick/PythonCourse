"""Создайте объект tuple, описывающий компьютер и распакуйте его в соответствующие переменные.
 Выведите переменные вызвав функцию print() один раз"""

tuple_pc = ('CPU Intel i5', 'RAM 8gb', 'Graphics AMD Radeon Pro 5500M')
cpu_pc, ram_pc, graphics_pc = tuple_pc
print('{}, {}, {}.'.format(cpu_pc, ram_pc, graphics_pc))