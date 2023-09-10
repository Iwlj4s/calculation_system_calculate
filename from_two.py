def binary_to_octal(binary_number):
    # --- From 2 To 8 --- #
    try:
        decimal_number = int(binary_number, 2)

        octal_representation = oct(decimal_number)

        return octal_representation[2:]

    except ValueError:
        return "Incorrect number format in binary number system"


def binary_to_decimal(binary_number):
    # --- From 2 To 10 --- #
    try:
        decimal_representation = int(binary_number, 2)

        return decimal_representation

    except ValueError:
        return "Incorrect number format in binary number system"


def binary_to_hex(binary_number):
    # --- From 2 To 16 --- #
    try:
        decimal_number = int(binary_number, 2)

        hex_representation = hex(decimal_number)

        return hex_representation[2:]

    except ValueError:
        return "Incorrect number format in binary number system"

