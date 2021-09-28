def main():
    #escribe tu código abajo de esta línea
    n = int(input())
    lista1=[]
    lista2=[]
    
    if n>0:
        for c in range (n):
            elemento=input()
            lista1.append(elemento)
            if (elemento in lista2)==False:
                lista2.append(elemento)
        print(lista1)
        print(lista2)
    else:
        print('Error')

if __name__=='__main__':
    main()
