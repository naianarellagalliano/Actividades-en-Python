nombre = input("Ingrese el nombre del cliente: ")
valor_compra = float(input("Ingrese el valor de la compra: "))
descuento = 0 

if valor_compra <80:
    print("Hola", nombre, "El valor a pagar es: $", valor_compra)
elif 80 <= valor_compra <=150:
    descuento = valor_compra * 0.1
elif 150 <= valor_compra <=300:
    descuento = valor_compra * 0.15
elif 300 <= valor_compra < 500:
    descuento = valor_compra * 0.2

precio_final = (valor_compra - descuento)
print("Compra sin descuento: ", valor_compra, "Compra con descuento: ", precio_final)

'''
Angel Mario Villa Lopez realizó una compra de 455 usd.
Su compra con descuento es de: 364.0
Rosa Diaz realizó una compra de 105 usd.
Su compra con descuento es de: 94.5
Dilan Gonzales realizó una compra de 250 usd.
Su compra con descuento es de: 212.5
Kelly Daza realizó una compra de 430 usd. 
Su compra con descuento es de: 344.0
'''