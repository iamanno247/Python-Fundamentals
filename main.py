# Line 1 of the input is a whole number, line 2 is a decimal number.
whole_text = input()
decimal_text = input()

# TODO: turn the two lines of text into numbers and add them up
total = int(whole_text) + float(decimal_text)

print(total)   # the sum, as a decimal
print(int(total))   # the same sum with the fraction chopped off toward zero
print(f"{int(whole_text)} + {float(decimal_text)} = {total}")   # the report line
