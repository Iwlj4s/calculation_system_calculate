def hex_to_binary(hex_number):
    # --- From 16 To 2 --- #
    try:
        decimal_number = int(hex_number, 16)

        binary_representation = bin(decimal_number)

        return binary_representation

    except ValueError:
        return "Incorrect number format in hexadecimal number system"


def hex_to_octal(hex_number):
    # --- From 16 To 8 --- #
    try:
        decimal_number = int(hex_number, 16)

        octal_representation = oct(decimal_number)

        return octal_representation

    except ValueError:
        return "Incorrect number format in hexadecimal number system"


def hex_to_decimal(hex_number):
    # --- From 16 To 10 --- #
    try:
        decimal_representation = int(hex_number, 10)

    except ValueError:
        return "Incorrect number format in hexadecimal number system"