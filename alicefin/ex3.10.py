for num in range(2, 101):
    e_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            e_primo = False
            break
    if e_primo:
        print(num)