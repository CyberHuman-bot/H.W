#I HAD TO STUY BINARY FOR THIS
n = int(input("Enter a number : "))

if n == 0:
    print("ANOTHER NUMBER")
else:
    p = 0
    pow_val = 1
    while pow_val * 2 <= n:
        pow_val *= 2
        p += 1

    bits = ""

    for exp in range(p, -1, -1):
        cur_pow = 1
        count = 0
        while count < exp:
            cur_pow *= 2
            count += 1

        if cur_pow <= n:
            bits += "1"
            n -= cur_pow
        else:
            bits += "0"

    print("Binary:", bits)
