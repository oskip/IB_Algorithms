import hashlib

print hashlib.sha256("fox").hexdigest()


A = 1111
A += 2222 << 16

print A & 0xFFFFFFFF


def pow(x, n):
    if n < 0: return pow(1/x, -n)
    if n == 0: return 1
    if n == 1: return x

    y = 1
    while n > 1:
        if n % 2 == 0:
            x = x*x
            n /= 2
        else:
            y = x*y
            x = x*x
            n = (n-1)/2
    return x*y

print pow(732908723409872389742394728834, 3016)
print 732908723409872389742394728834**3016