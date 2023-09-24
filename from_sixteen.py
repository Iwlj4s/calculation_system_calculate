def hex_to_binary(hex_number):
    try:
        decimal_number = int(hex_number, 16)
        binary_representation = bin(decimal_number)
        return binary_representation[2:]
    except ValueError:
        return "Incorrect number format in hexadecimal number system"


def hex_to_octal(hex_number):
    try:
        decimal_number = int(hex_number, 16)
        octal_representation = oct(decimal_number)
        return octal_representation[2:]
    except ValueError:
        return "Incorrect number format in hexadecimal number system"


def hex_to_decimal(hex_number):
    try:
        decimal_representation = int(hex_number, 16)
        return decimal_representation
    except ValueError:
        return "Incorrect number format in hexadecimal number system"
