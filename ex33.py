i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    i += 1
    print("Numbers now:", numbers)

for num in numbers:
    print("\v\t", num)