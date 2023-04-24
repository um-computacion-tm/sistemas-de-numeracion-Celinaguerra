def octal2binario(oct):
    diccionario_oct = {"0": "000", "1": "001","2": "010","3": "011","4":"100","5":"101","6":"110",
                       "7":"111"}
    octal = ""
    
    for i in oct:
        if i in diccionario_oct:
            bin = diccionario_oct[i]
            octal += bin
    return octal

def hexadecimal2binario(hex):
    diccionario_hex = {"0": "0000", "1": "0001","2": "0010","3": "0011","4":"0100","5":"0101","6":"0110",
                       "7":"0111","8":"1000","9":"1001", "A":"1010","B":"1011","C":"1100","D":"1101",
                       "E":"1110","F":"1111"}
    hexadecimal = ""
    
    for i in hex:
        if i in diccionario_hex:
            bin = diccionario_hex[i]
            hexadecimal += bin
    return hexadecimal
