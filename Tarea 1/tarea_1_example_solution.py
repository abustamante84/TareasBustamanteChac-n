def operation_selector(num1, num2, op):
    # Verifica si num1 y num2 son numeros enteros
    if not (isinstance(num1, int) and not isinstance(num1, bool)) \
            or not (isinstance(num2, int) and not isinstance(num2, bool)):
        return -50, None

    # Verifica si el caracter op es un string
    if not isinstance(op, str):
        return -60, None

    # Verifica si el caracter op es uno de los permitidos
    if op not in ["+", "-", "*", "&"]:
        return -70, None

    # Realiza la operación segun lo elegido
    if op == "+":
        resultado = num1 + num2
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    elif op == "&":
        resultado = num1 & num2

    # Si no hay errores retorna un 0 y el resultado
    return 0, resultado


def calculo_promedio(lista_valores):
    # Verifica que el tamaño de la lista no sea mayor a 10 elementos
    if len(lista_valores) > 10:
        return -90, None

    # Verifica que todos los elementos de la lista sean numeros
    for valor in lista_valores:
        if not (isinstance(valor, (int, float))
                and not isinstance(valor, bool)):
            return -80, None

    # Calcula el promedio de los valores en la lista
    promedio = sum(lista_valores) / len(lista_valores) if lista_valores else 0

    # Si no hay errores retorna un 0 y el resultado
    return 0, promedio
