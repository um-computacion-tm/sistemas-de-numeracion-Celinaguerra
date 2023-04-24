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

def octal2decimal (oct):
    oct = str(oct)
    decimal = 0
    potencia = 0
    for i in range(len(oct)-1,-1,-1):
        decimal += int(oct[i]) * 8**potencia
        potencia += 1
    decimal = str(decimal)
    return decimal

def hexadecimal2decimal(hex):
    hex = str(hex)
    decimal = 0
    potencia = 0
    hex_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    hex_dict_inv = {v: k for k, v in hex_dict.items()}
    for i in range(len(hex)-1,-1,-1):
        decimal += hex_dict[hex[i]] * 16**potencia
        potencia += 1
    decimal = str(decimal)
    return decimal