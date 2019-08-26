def multiplica(operacion):
    resultado = 1
    operadores = operacion.split("*")
    for value in operadores:
        resultado *= int(value)
    return resultado  

cadena = str(input())
separaciones = cadena.split("+")
i = 0;
for value in separaciones:
    if (value.find("*") !=-1):
        resultado = multiplica(value)
        separaciones[i] = resultado
    i += 1
resultado = 0
for value in separaciones:
    resultado += int(value)
print(resultado)
       