def pitagoras(a, b):
    return (a ** 2 + b ** 2) ** 0.5

print(pitagoras(3, 4))



print((lambda a, b: (a ** 2 + b ** 2) ** 0.5)(3, 4))

[].sort(key=lambda a: a[1])