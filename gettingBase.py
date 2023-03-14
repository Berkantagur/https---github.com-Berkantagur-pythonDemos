#Base retrieval according to the base and basis information entered by the user

base = int(input("Base: "))
basis = int(input("Basis: "))
result = 1

for i in range(1, base + 1, 1):
    result *= basis

print(result)

