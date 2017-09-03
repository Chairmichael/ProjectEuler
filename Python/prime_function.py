
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or not n%2: return False
    if n < 9: return True
    if not n%3: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if not n%f: return False
        if not n%(f+2): return False
        f +=6
    return True