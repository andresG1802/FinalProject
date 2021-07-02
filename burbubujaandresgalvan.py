a=int(input('Digite el primer numero:'))
b=int(input('Digite el segundo numero:'))
c=int(input('Digite el tercer numero:'))
d=int(input('Digite el cuarto numero:'))
e=int(input('Digite el quinto numero:'))
f=int(input('Digite el sexto numero:'))
g=int(input('Digite el septimo numero:'))
h=int(input('Digite el octavo numero:'))
i=int(input('Digite el noveno numero:'))


arreglo = [a,b,c,d,e,f,g,h,i] 

band =False
while band == False:
    band= True
    for i in range(len(arreglo)-1):
        if arreglo[i] > arreglo[i + 1]:
            auxiliar = arreglo[i]
            arreglo[i] = arreglo[i+1]
            arreglo[i+1]= auxiliar
            band= False
print(arreglo)