#Actividad 4 Conversor de monedas
print("Bienvenido al conversor de monedas!!  \n")

def conversor(moneda_actual, valor, moneda_a_convertir):
    if moneda_actual == 1:

        def dolarTo():
            if moneda_a_convertir == "1":
                print(f'{valor} dolares equivale a ${valor * 3750} Pesos Argentinos')
            elif moneda_a_convertir == "2":
                  print(f'{valor} dolares equivale a ${valor * 6.37} Yuanes')
            elif moneda_a_convertir == "3":
                    print(f'{valor} dolares equivale a ${valor * 0.76} Libras Esterlinas')
            else:
                 print("No se reconoce la moneda a convertir")
        
        dolarTo()
    elif moneda_actual == 2:
            
        def euroTo():
            if moneda_a_convertir == "1":
                print(f'{valor} euros equivale a ${valor * 4000} Pesos Argentinos')
            elif moneda_a_convertir == "2":
                  print(f'{valor} euros equivale a ${valor * 6.93} Yuanes')
            elif moneda_a_convertir == "3":
                    print(f'{valor} euros equivale a ${valor * 0.83} Libras Esterlinas')
            else:
                 print("No se reconoce la moneda a convertir")
        
        euroTo()
    else:
         print("No se reconoce la moneda a convertir")

moneda_actual = int(input("Ingrese su moneda actual: \n 1.Dolar \n 2.Euro \n"))

valor = float(input("Ingrese el valor a convertir: \n"))

moneda_a_convertir = input("¿A qué moneda quiere convertir?: \n 1.Pesos Argentinos \n 2.Yuanes \n 3.Libras Esterlinas \n")

conversor(moneda_actual, valor, moneda_a_convertir)

'''
1- ¿Cuánto equivalen 50 dolares en pesos argentinos?
   1- 50 Dolares equivalen a $187500.0 pesos argentinos
2- ¿Cuánto equivalen 30 euros en yuanes?
   2- 30 Euros equivalen a $207.89 Yuanes
3- ¿Cuánto equivalen 15 euros en libras esterlinas?
   3- 15 Euros equivalens a $12.45 Libras Esterlinas
'''
