a=int(input("ingrese el año"))

if a%400==0 or a%4==0 and a%100!=0:
    print("es año bisiesto")
else:
    print(" no es año bisiesto")
