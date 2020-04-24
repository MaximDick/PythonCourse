"""task1.If we write out all natural numbers less than 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
The sum of these numbers is 23.
Find the sum of all numbers less than 1000, multiples of 3 or 5."""
summa = 0
for number in range(1001):
    if  number % 3 == 0 and number % 5 == 0:
        summa = summa + number
        print('number: {},  summa: {}'.format(number, summa))
print('summa {}'.format(summa))