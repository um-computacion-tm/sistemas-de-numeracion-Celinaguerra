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