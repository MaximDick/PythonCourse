"""N школьников поделили K яблок поровну, не делящийся остаток остался в корзинке.
 Сколько яблок осталось в корзинке?"""
n = int(input("Введите n:"))
k = int(input("Введите k:"))
m = k % n
print(m)