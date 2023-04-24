def binario2decimal(bin):
    bin = str(bin)
    decimal = 0
    potencia = 0
    for i in range(len(bin)-1,-1,-1):
        if bin[i] == "1":
            decimal += 2**potencia
        potencia += 1
    decimal = str(decimal)
    return decimal

def binario2octal(bin):
    bin = str(bin)
    decimal = 0
    potencia = 0
    for i in range(len(bin)-1,-1,-1):
        if bin[i] == "1":
            decimal += 2**potencia
        potencia += 1
    resultado = ""
    octal = ""
    while decimal >=8:
        resto = decimal % 8
        decimal = decimal // 8
        div = str(resto)
        resultado += div
    resultado += str(decimal)
    octal = resultado[::-1]
    return octal

def binario2hexadecimal(bin):
    bin = str(bin)
    decimal = 0
    potencia = 0
    for i in range(len(bin)-1,-1,-1):
        if bin[i] == "1":
            decimal += 2**potencia
        potencia += 1
    hexadecimal = ""
    resultado = ""
    hex_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while decimal >= 16:
        resto = decimal % 16
        decimal = decimal // 16
        
        if resto in hex_dict:
            div = hex_dict[resto]
        else:
            div = str(resto)
        resultado += div
    if decimal in hex_dict:
        resultado += hex_dict[decimal]
    else:
        resultado += str(decimal)
    hexadecimal = resultado[::-1]
    return hexadecimal