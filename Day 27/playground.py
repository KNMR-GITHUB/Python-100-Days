def add(*values):
    sum = 0
    for x in values:
        sum += x

    return sum

print(add(1,2,3))