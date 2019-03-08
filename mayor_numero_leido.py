print("Numero mayor de 0 a 5")
a=0
for i in range(0,5):
  b=int(input("Digita un numero: "))
  if i==0:
    a=b
  if a<b:
    a=b

print("El mayor es " + str(a))  
    