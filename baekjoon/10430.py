abc = "5 8 4"

A, B, C = [int(s) for s in abc.split()]

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)