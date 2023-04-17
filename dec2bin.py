
def decimal2binario(dec):
    resultado = ""
    while dec >= 2:
        resto = dec % 2
        dec = dec // 2
    
        div = str(resto)
        resultado += div
    if dec == 1:
        resultado += "1"
    else:
        resultado += "0"
    if len(resultado)<8:
        cantidad = 8-len(resultado)
        resultado += "0"*cantidad
    total = resultado[::-1]
    return total