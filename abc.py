pesoLibra = float(input("Ingresa el peso en libras "))
tallaPulgada = float(input("Ingresa la altura en pulgadas "))

pesoKilo = pesoLibra/2.205
tallaMetro = tallaPulgada/ 39.37

imc = pesoKilo/tallaMetro**2
print ("El IMC es: ", imc)

if imc<18.5 :
    print ("Su observación es: Bajo peso")
elif 18.5<= imc <25:
    print ("Su observación es: Normal")
elif 25<= imc <30:
    print ("Su observación es: Sobrepeso")
else :
    print ("Su observación es: Obeso")

