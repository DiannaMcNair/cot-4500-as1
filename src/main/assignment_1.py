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

def terms_to_compute_series(x, tolerance):
    k=1
    i=1
    while i < 100:
        k += 1
        function = (-1)**k * (x**k / k**3)
        if abs(function) < tolerance:
            break
        i += 1
    print(i)
    return i

def bisection_method(a, b, tolerance):
    i = 1
    while i < 50:
        mid = (a+b)/2
        f_mid = mid**3 + 4*(mid**2) - 10
        f_a = a**3 + 4*(a**2) - 10
        f_b = b**3 + 4*(b**2) - 10

        case_1: bool = f_a > 0 and f_mid < 0
        case_2: bool = f_a < 0 and f_mid > 0
        
        if case_1 or case_2:
            b = mid
        else:
            a = mid

        if abs(a-b) <= tolerance:
            break
        i += 1

    print(i)

def newton_raphson(initial_guess, tolerance):
    x = initial_guess
    i = 1
    while i < 50:

      f_x = x**3 + 4*(x**2) - 10
      f_prime = 3*(x**2) + 8*x

      x_next = x-(f_x/f_prime)

      if abs(x - x_next) <= tolerance:
        break

      i+= 1
      x = x_next

    print(i)
    return x


num_1 = calculate_float("010000000111111010111001")
print(num_1)

chopped_num = three_digit_chop(num_1)
print(chopped_num)
rounded_num = three_digit_round(num_1)
print(rounded_num)

abs_error = abs(num_1 - rounded_num)
relative_error = abs(num_1 - rounded_num)/abs(num_1)
print(abs_error, relative_error)

#infinite series, (-1)^k * (x^k / k^3)
#find min terms needed to solve for x=1 w/ error 10^-4
terms_to_compute_series(1, 10**(-4))

#Determine number of iterationst o solve f(x) = x^3 + 4x^2 – 10 = 0
#accuracy 10^-4 using a = -4 and b = 7
bisection_method(-4, 7, 10**(-4))
newton_raphson(7, 10**(-4))

