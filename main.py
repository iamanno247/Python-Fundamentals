total = 0

# TODO: keep reading integers and adding them to total.
# Stop as soon as the value you read is the sentinel, and leave it out of the total.

while True:
    num = int(input())
    if num == 0:
        break
    else:
        total += num
        continue
print(total)