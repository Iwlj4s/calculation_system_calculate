def decimal_to_binary(decimal_number):
    try:
        decimal_number = int(decimal_number)
        binary_representation = bin(decimal_number)
        return binary_representation[2:]

    except ValueError:
        return "Incorrect number format in decimal number system"


def decimal_to_octal(decimal_number):
    # --- From 10 To 8 --- #
    try:
        decimal_number = int(decimal_number)
        octal_representation = oct(decimal_number)

        return octal_representation

    except ValueError:
        return "Incorrect number format in decimal number system"


def decimal_to_hex(decimal_number):
    try:
        decimal_number = int(decimal_number)
        hex_representation = hex(decimal_number)
        return hex_representation[2:]
    except ValueError:
        return "Incorrect number format in decimal number system"





