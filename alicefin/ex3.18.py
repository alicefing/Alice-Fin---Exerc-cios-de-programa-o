n = int(input("Digite o valor de n para a sequência de Fibonacci: "))

a, b = 0, 1

print("Sequência de Fibonacci até o {}º termo:".format(n))
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b