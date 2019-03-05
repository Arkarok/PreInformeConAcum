print("Suma del primer y ultimo numero de un bucle for")

suma=0

for num in range(1,11):
  print(num)
  if num==1:
    suma+=num
  if num==10:
    suma+=num
    
print("La suma del primer y ultimo numero es " + str(suma))    
print("Final del programa")

