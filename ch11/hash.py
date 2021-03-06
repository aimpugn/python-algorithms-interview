# https://myshell.co.uk/blog/2018/11/python-f-string-formatting-cheatsheet/ 
def print_bitwise(a, op = None, b = None):
    print('============================================')
    print("a: ", a, ",op: ", op, ",b: ", b)
    if a:
        a_in_64b = f"{a:64b}"
        a_in_64b_len = str(len(a_in_64b) - a_in_64b.count(' '))
        print(a_in_64b + " [" + a_in_64b_len + "]")
    if b:
        b_in_64b = f"{b:64b}"
        b_in_64b_len = str(len(b_in_64b) - b_in_64b.count(' '))
        print(b_in_64b + " [" + b_in_64b_len + "]")

    if a and b and op:
        print('--------------------------------------------')
        if op == '&':
            result = a & b
        elif op == '|':
            result == a | b
        result_in_64b = f"{result:64b}"
        result_in_64b_len = str(len(result_in_64b) - result_in_64b.count(' '))

        print(result_in_64b + " [" + result_in_64b_len + "]")
        print(f"{result:n}")


print_bitwise(222)
print_bitwise(-222)
print_bitwise(0x7FFFFFFF)
print_bitwise(-0x80000000)
print_bitwise(222, '&', 0x7FFFFFFF)
print_bitwise(2147483648, '&', 0x7FFFFFFF)
print_bitwise(-2147483648, '&', 0x7FFFFFFF)
print_bitwise(98989898989898, '&', 0x7FFFFFFF)
print_bitwise(-222, '&', 0x7FFFFFFF)