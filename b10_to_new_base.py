def b10_to_new_base(b10num, newbase):
    newstr = ""
    while b10num > 0:
        newstr = str(b10num%newbase)+newstr
        b10num = b10num // newbase
    return newstr

while True:
    b10 = int(input("Enter a b10 (decimal) number: "))
    base = int(input("Enter a new base: "))
    print(b10_to_new_base(b10, base))

def to_b10(binum, newbase):
    newstr1 = ""
    