while True:
    print("\n--- Calculadora Sencilla ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        match opcion:
            case "1":
                print("Resultado:", num1 + num2)
            case "2":
                print("Resultado:", num1 - num2)
            case _:
                print("Opción inválida. Intenta de nuevo.")
            case "3":
                print("Resultado:", num1 * num2)

    except ValueError:
        print("Entrada inválida. Por favor, ingresa números.")
        continue

