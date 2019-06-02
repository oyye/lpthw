the_count = [1, 2, 3, 4, 5, 6]
fruites = ["apple", 'orange', "pear"]
change = [1, "pennies", 2, "dimes"]

for count in the_count:
    print(f"This is count: {count}")

for fruit in fruites:
    print(f"A fruite of type : {fruit}")

for i in change:
    print(f"I got {i}")

elements = []
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f'Element was: {i}')