power = 3
base = 2
zero = 0

print(type(zero))

# doesn't work properly
print(base + power * zero)

# fixed
print (str(base) + power * str(zero))
