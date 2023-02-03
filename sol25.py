# Setup
file = open('../data/data00.txt', 'r')
file = open('../data/data25.txt', 'r')
nums = file.read().split("\n")
file.close()

total = 0
for num in nums:
    dec = 0
    pow = 0
    for i in range(len(num)-1, -1, -1):
        if num[i] == "=": digit = -2
        elif num[i] == "-": digit = -1
        else: digit = int(num[i])
        dec += ((5**pow) * digit)
        pow += 1
    total += dec

print(f"Decimal total: {total}")

snafu = ""
pow = 1
carry = 0
while total > 0 or carry > 0:
    print("Power:", pow)
    rem = (total % (5**pow))
    total -= rem
    print("Total left:", total)
    digit = rem // (5**(pow-1))
    if carry:
        digit += 1
        carry = 0
    if digit > 2:
        if digit == 3:
            digit = "="
            carry = 1
        elif digit == 4:
            digit = "-"
            carry = 1
        elif digit == 5:
            digit = "0"
            carry = 2
            
        carry = True
        print("Carry")
    else:
        digit = str(digit)
    print(carry)
    print("Digit:", digit)
    snafu = digit + snafu
    print("Snafu:", snafu)
    pow += 1
    print()
print("Snafu:", snafu)