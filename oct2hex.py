def octal2hexadecimal(oct):
    oct = str(oct)
    hex_dict = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
        6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
        11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    decimal = 0
    for i in range(len(oct)):
        decimal += int(oct[-(i+1)]) * 8**i
    hexadecimal = ''
    while decimal > 0:
        hexadecimal = hex_dict[decimal % 16] + hexadecimal
        decimal = decimal // 16
    return hexadecimal