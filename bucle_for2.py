print("Suma de los primeros numeros pares en el rango de (1,10)")

suma=0

for num in range(1,11):
  print(num)
  if num%2==0:
    suma+=num
    
print("La suma de los numeros pares en el rango de (1,10) es " + str(suma))    
print("Final del programa")
