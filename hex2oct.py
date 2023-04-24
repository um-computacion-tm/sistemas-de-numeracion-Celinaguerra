def hexadecimal2octal(hex):
    hex_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    oct_dict = {
        0: '0', 1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7'
    }
    decimal = 0
    for i in range(len(hex)):
        decimal += hex_dict[hex[-(i+1)]] * 16**i
    octal = ''
    while decimal > 0:
        octal = oct_dict[decimal % 8] + octal
        decimal = decimal // 8
    return octal