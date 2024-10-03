contador = 0 

print("Calculadora de Indice de Masa corporal - IMC")

while contador !=2:
  contador = int(input("¿Quieres seguir calculando el IMC? 1.SI y 2.NO \n"))

if contador ==1: 
  estatura = float(input("Ingrese su estatura en metros: "))
  peso = float(input("Ingrese su peso en kilogramos: "))
  resultado = round(peso/(estatura**2), 2)

  if resultado < 18.5:
    print(f'IMC {resultado} = Bajo de peso')
  elif 18.5 < resultado < 24.99:
    print(f'IMC {resultado} = Peso normal')
  elif 25 < resultado < 30:
    print(f'IMC {resultado} = Sobrepeso')
  elif resultado > 30:
    print(f'IMC {resultado} = Obesidad')

elif contador ==2:
  print("Hasta pronto!!")

print("Gracias por utilizar la calculadora de IMC!")