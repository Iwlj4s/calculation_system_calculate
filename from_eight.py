def octal_to_binary(octal_number):
    # --- From 8 To 2 --- #
    try:
        decimal_number = int(octal_number, 8)

        binary_representation = bin(decimal_number)

        return binary_representation[2:]

    except ValueError:
        return "Incorrect number format in octal number system"


def octal_to_decimal(octal_number):
    # --- From 8 To 10 --- #
    try:
        decimal_representation = int(octal_number, 8)

        return decimal_representation

    except ValueError:
        return "Incorrect number format in octal number system"


def octal_to_hex(octal_number):
    # --- From 8 To 16 --- #
    try:
        decimal_number = int(octal_number, 8)

        hex_representation = hex(decimal_number)

        return hex_representation

    except ValueError:
        return "Incorrect number format in octal number system"
