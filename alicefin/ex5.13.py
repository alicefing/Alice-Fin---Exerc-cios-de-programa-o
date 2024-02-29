lista1 = [10, 20, 30, 40]
lista2 = [50, 60, 70, 80]

medias = [(lista1[i] + lista2[i]) / 2 for i in range(len(lista1))]
print(f"{medias} --> é médias dos elementos correspondentes")