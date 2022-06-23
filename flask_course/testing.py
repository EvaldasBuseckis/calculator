def ar_keliamieji() -> list:
    for x in range (1900, 2100):
        if x % 400 == 0 or x % 100 != 0 and x % 4 == 0:
            return list(x)
        else:
            return None

print(ar_keliamieji())
