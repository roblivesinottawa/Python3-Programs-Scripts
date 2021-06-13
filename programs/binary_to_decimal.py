def binary_to_decimal(n):
    num = n
    dec_value = 0

    base = 1
    temp = num

    while(temp):
        last_digit = temp % 10
        temp = int(temp / 10)

        dec_value += last_digit * base

        base = base * 2

    return dec_value

result = binary_to_decimal(10010101)
print(result)