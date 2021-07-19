print("not True: {}".format(not True))
print("not False: {}".format(not False))

print("~ True: {}".format(~ True)) # -2
print("~ False: {}".format(~ False)) # -1

print("True and True: {}".format(True and True))
print("True and False: {}".format(True and False))
print("False and True: {}".format(False and True))
print("False and False: {}".format(False and False))


print("True & True: {}".format(True & True))
print("True & False: {}".format(True & False))
print("False & True: {}".format(False & True))
print("False & False: {}".format(False & False))

print("True or True: {}".format(True or True))
print("True or False: {}".format(True or False))
print("False or True: {}".format(False or True))
print("False or False: {}".format(False or False))

print("True | True: {}".format(True | True))
print("True | False: {}".format(True | False))
print("False | True: {}".format(False | True))
print("False | False: {}".format(False | False))


print("(True and not True) or (not True and True): {}".format((True and not True) or (not True and True)))
print("(True and not False) or (not True and False): {}".format((True and not False) or (not True and False)))
print("(False and not True) or (not False and True): {}".format((False and not True) or (not False and True)))
print("(False and not False) or (not False and False): {}".format((False and not False) or (not False and False)))

print("True ^ True: {}".format(True ^ True))
print("True ^ False: {}".format(True ^ False))
print("False ^ True: {}".format(False ^ True))
print("False ^ False: {}".format(False ^ False))

def decimal_to_binary(num, bit = 32):
    result = ""
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result.rjust(bit, "0")

print(decimal_to_binary(16, 8))

print("bin(0b0110 + 0b0010) = bin({} + {}) = {} = {}".format(0b0110, 0b0010, bin(0b0110 + 0b0010), 0b0110 + 0b0010))
print("bin(0b0011 * 0b0101) = bin({} * {}) = {} = {}".format(0b0011, 0b0101, bin(0b0011 * 0b0101), 0b0011 * 0b0101))
print("bin(0b1101 >> 2) = bin({} >> 2) = {} = {}".format(0b1101, bin(0b1101 >> 2), 0b1101 >> 2))
print("bin(0b01001011 >> 1) = bin({} >> 1) = {} = {}".format(0b01001011, bin(0b01001011 >> 1), 0b01001011 >> 1))
print("bin(0b1101 << 2) = bin({} << 2) = {} = {}".format(0b1101, bin(0b1101 << 2), 0b1101 << 2))
print("bin(~0b1100) = bin(~{}) = {} = {}".format(0b1100, bin(~0b1100), ~0b1100))
print("bin(0b0101 ^ ~0b1100) = bin({} ^ {}) = bin({} ^ {}) = {} = {}".format(bin(0b0101), bin(~0b1100), 0b0101, ~0b1100, bin(0b0101 ^ ~0b1100), 0b0101 ^ ~0b1100))


MASK = 0xF # 15 = 1111
print("bin(1 & MASK) = {}".format(bin(1 & MASK)))
print("bin(7 & MASK) = {}".format(bin(7 & MASK)))
print("bin(-8 & MASK) = {}".format(bin(-8 & MASK)))
print("bin(-7 & MASK) = {}".format(bin(-7 & MASK)))
print("bin(-1 & MASK) = {}".format(bin(-1 & MASK)))

print(~0b1001)
print(bin(~7))