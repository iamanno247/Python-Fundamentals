n = int(input())

# TODO: print the ten lines of the table for n, one line per product.
# Loop over the numbers 1 through 10 and build each line with an f-string.
# Nothing is printed yet, so every test fails until you add the loop.

for x in range (1, 11):
  multi = n * x
  print(f"{n} x {x} = {multi}")
