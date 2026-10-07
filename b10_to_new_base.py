def b10_to_new_base(b10num, newbase):
    newstr = ""
    while b10num > 0:
        newstr = str(b10num%newbase)+newstr
        b10num = b10num // newbase
    return newstr

def to_b10(binum, base):
    decimal = 0
    for digit in binum:
        decimal = decimal*base + int(digit)
    return decimal

while True:
    b10 = int(input("Enter a b10 (decimal) number: "))
    base = int(input("Enter a new base: "))
    newnum = b10_to_new_base(b10, base)
    print(newnum)
    print(to_b10(newnum, base))

