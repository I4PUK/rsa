import random
# Алгоритм Евклида(нахождение наибольшего общего делителя)
def NOD(a, b):
    if (b == 0):
        return a
    return NOD(b, a % b)


# Тест простоты числа Рабин - Миллера, возвращает истину если число простое
def RabinMillerTest(n, r=15):
    if n != int(n):
        return False
    n = int(n)

    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


# Бинарное возведение в степень по модулю. (Вычисляет  a^n mod m)
def Exponetial(a, n, m):
    res = 1
    p = a % m
    while n:
        if (n & 1):
            res = (res * p) % m
        n >>= 1
        p = (p * p) % m
    return res


# Подбирает (g, x, y) такие, что a * x + b * y = g
def gcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


# x = exGCD(b) mod n, (x * b) % n == 1
# расширенный алгоритм GCD для поиска модулярных инверсий:
def exGCD(a, b):
    g, x, _ = gcd(a, b)
    if g == 1:
        return x % b


# random.getrandbits - возвращает N случайных бит
p = random.getrandbits(256)
while (RabinMillerTest(p) == False):
    p = random.getrandbits(256)

q = random.getrandbits(256)
while (RabinMillerTest(q) == False):
    q = random.getrandbits(256)
print('p=', p)
print('q=', q)
# модуль
n = p * q
print('n=', n)
# функцию Эйлера
fi = (p - 1) * (q - 1)
print('fi=', fi)
# число e
print('Введите число e: ')
e = int(input())
while NOD(e, fi) != 1:
    e = random.randint(1, fi)
print('e=', e)
# алгоритм GCD
d = exGCD(e, fi)
print('d=', d)
# исходное сообщение
message = 10
print('Сообщение - ', message)
EncryptedMessage = Exponetial(message, e, n)
print('Зашифрованное сообщение - ', EncryptedMessage)
Decryption = Exponetial(EncryptedMessage, d, n)
print('Расшифрованное сообщение - ', Decryption)
