def sum(number_one, number_two):
    number_one_int = convert_int(number_one)
    number_two_int = convert_int(number_two)

    result = number_one_int + number_two_int

    return result

def convert_int(number_str):
    converted_int = int(number_str)
    return converted_int


ans = sum("1", "2")
