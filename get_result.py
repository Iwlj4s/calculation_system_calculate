import from_two
import from_eight
import from_ten
import from_sixteen


def get_res(value_from, value_to, number):
    # --- From 2 --- #
    if value_from == "2" and value_to == "8":
        return from_two.binary_to_octal(number)

    elif value_from == "2" and value_to == "10":
        return from_two.binary_to_decimal(number)

    elif value_from == "2" and value_to == "16":
        return from_two.binary_to_hex(number)

    # --- From 8 --- #
    if value_from == "8" and value_to == "2":
        return from_eight.octal_to_binary(number)

    elif value_from == "8" and value_to == "10":
        return from_eight.octal_to_decimal(number)

    elif value_from == "8" and value_to == "16":
        return from_eight.octal_to_hex(number)

    # --- From 10 --- #
    if value_from == "10" and value_to == "2":
        return from_ten.decimal_to_binary(number)

    elif value_from == "10" and value_to == "8":
        return from_ten.decimal_to_octal(number)

    elif value_from == "10" and value_to == "16":
        return from_ten.decimal_to_hex(number)

    # --- From 16 --- #
    if value_from == "16" and value_to == "2":
        return from_sixteen.hex_to_binary(number)

    elif value_from == "16" and value_to == "8":
        return from_sixteen.hex_to_octal(number)

    elif value_from == "16" and value_to == "10":
        return from_sixteen.hex_to_decimal(number)

    else:
        return number
