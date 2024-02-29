data_string = (input("Digite uma data: "))
mes, dia, ano = data_string.split ('/')

if len (data_string) != 10:
    print ("A data deve ter 10 caracteres") 

mes = int(mes)
dia = int (dia)
ano = int (ano)


if (1 <= mes <= 12) and (1 <= dia <= 31) and (1000 <= ano <= 9999):
    if (mes in {1, 3, 5, 7, 8, 10, 12} and 1 <= dia <= 31) or \
        (mes in {4, 6, 9, 11} and 1 <= dia <= 30) or \
        (mes == 2 and ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0) and 1 <= dia <= 29) or \
        (mes == 2 and ((ano % 4 != 0 or ano % 100 == 0) and ano % 400 != 0) and 1 <= dia <= 28):
        print ("Com Formato mm/dd/aaa")
    else:
        print ("Com formato inválido") 
else:           
    print ("Com formato inválido")        