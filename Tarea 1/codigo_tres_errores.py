import random


def super():
    print("Hola!, con un número aleatorio obtendrás un descuento especial. \
      \nSi tu número es mayor a 50 es del 20% y si es menor, sería del 15% \n")
    input("Presiona ENTER para participar \n")

    num = random.randint(1, 100)

    if num < 50:
        print("Tu número es " + str(num) + ". Descuento del 15%.")
        return 0
    else:
        print("Tu número es " + str(num) + ". Descuento del 20%.")
        return 0
