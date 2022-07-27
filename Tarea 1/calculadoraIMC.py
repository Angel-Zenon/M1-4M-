
numeroDePersonas = int(input("Personas: "))

while numeroDePersonas > 0:
    nombre = input("""・  Ingresa  tu nombre: """)
    edad = int(input("""・  Introduce   tu  edad: """))
    altura = float(input("・  Introduce tu  altura en metros: "))
    peso = float(input("・  Introduce tu peso en kilogramos: "))

    if(edad < 18):
        print("""      |%s| 
    Eres menor de edad """ %(nombre))
    else:
        print("""      |%s| 
    Usted es mayor de edad """ %(nombre))

    imc = peso / altura**2 
    print(f"""Su indice de masa corporal es de:
            |{imc: .2f}|
            """ )

    if imc >= 0 and imc <= 15.99:
        print("Por lo tanto, %s  Usted tiene delgadez severa 😞" %(nombre))
    elif imc >= 16.00 and imc <= 16.99:
        print("Por lo tanto, %s Usted tiene delgadez moderada 😞" %(nombre))
    elif imc >= 17.00 and imc <= 18.49:
        print("Por lo tanto, %s Usted tiene delgadez leve 😔" %(nombre))
    elif imc >= 18.50 and imc <= 24.99:
        print("Por lo tanto, %s Usted tine un IMC normal 😀" %(nombre))
    elif imc >= 25.00 and imc <= 29.99:
        print("Lamentablemente %s Tiene sobrepeso" %(nombre))
    elif imc >= 30.00 and imc <= 34.99:
        print("Lamentablemente %s Usted tiene obesidad leve 😔" %(nombre))
    elif imc >= 35.00 and imc <= 39.99:
        print("Lamentablemente %s Usted tiene obesidad media 😞" %(nombre))
    elif imc >= 40.00:
        print("Lamentablemente %s Usted tiene obesidad morbida 😞" %(nombre))
    numeroDePersonas = numeroDePersonas - 1

