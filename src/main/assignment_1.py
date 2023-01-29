import math

#use double precision, calculate and format to 5 decimal places
    #0 10000000111 111010111001
#pass in binary as string
def calculate_float(binary_string: str):
    sign = binary_string[0]
    exponent = binary_string[1:12]
    mantissa = binary_string[12:]

    exponent_int = int(exponent, 2)
    result = 1
    i = 1
    for digit in mantissa:
        if digit == "1":
            result += ((1/2)**i)
        i += 1

    result = result * (2**(exponent_int-1023))
    if sign == "1":
        result = result * (-1)

    return result


def three_digit_chop(og_num: float):
    string_num = str(og_num).split(".")
    digits = len(string_num[0])
    normalized = og_num / (10**digits)

    result = math.trunc(normalized*1000)/1000
    print(result)

    return result * (10**digits)

def three_digit_round(og_num: float):
    string_num = str(og_num).split(".")
    digits = len(string_num[0])
    normalized = og_num / (10**digits)

    result = math.trunc(normalized*1000 + .5)/1000
    print(result)

    return result * (10**digits)



num_1 = calculate_float("010000000111111010111001")
print(num_1)

chopped_num = three_digit_chop(num_1)
print(chopped_num)
rounded_num = three_digit_round(num_1)
print(rounded_num)

abs_error = abs(num_1 - rounded_num)
relative_error = abs(num_1 - rounded_num)/abs(num_1)
print(abs_error, relative_error)
    