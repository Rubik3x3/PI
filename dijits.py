import os
from decimal import *

getcontext().prec = int(input("Ingrese la cantidad de digitos de Pi a calcular: "))

k = 0
r = 0

potencias = Decimal(1)
anterior = 0

while True:

    r += Decimal((Decimal(1)/potencias)*(Decimal(Decimal(4)/Decimal(8*k+1))-Decimal(Decimal(2) /
                 Decimal(8*k+4))-Decimal(Decimal(1)/Decimal(8*k+5))-Decimal(Decimal(1)/Decimal(8*k+6))))
    k += 1

    potencias *= 16
    os.system("clear")
    print(r)

    if anterior == r:
        break
    anterior = r
