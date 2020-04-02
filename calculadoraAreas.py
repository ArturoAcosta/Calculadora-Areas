opcion = 0
while opcion != 4:
    print ("Calculadora de areas \n")
    print ("1. Triangulo")
    print ("2. Circulo")
    print ("3. Rectangulo")
    print ("4. Salir")

    # Get the user’s choice:
    opcion = int(input("Selecciona una opcion 1-4: "))

    # Calculate the area:
    if opcion == 1:
        altura = int(input("Ingresa la altura: "))
        base = int(input("Ingresa la base: "))
        area = 0.5*(altura*base)
        print ("El area es: ", area)  
    if opcion == 2:
        radio = int(input("Ingresa el radio: "))
        area = 3.14159*(radio**2)
        print ("El area es: ", area)
    if opcion == 3:
        altura = int(input("Ingresa la altura: "))
        base = int(input("Ingresa la base: "))
        area = altura*base
        print ("El area es: ", area)
    if opcion == 4:
        break