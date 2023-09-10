def decimal_to_binary(decimal_number):
    # --- From 10 To 2 --- #
    try:
        binary_representation = bin(decimal_number)

        return decimal_number

    except ValueError:
        return "Incorrect number format in decimal number system"


def decimal_to_octal(decimal_number):
    # --- From 10 To 8 --- #
    try:
        octal_representation = oct(decimal_number)

        return octal_representation

    except ValueError:
        return "Incorrect number format in decimal number system"


def decimal_to_hex(decimal_number):
    # --- From 10 To 16 --- #
    try:
        hex_representation = hex(decimal_number)

        return hex_representation

    except ValueError:
        return "Incorrect number format in decimal number system"





