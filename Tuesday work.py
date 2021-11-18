# Tuesday Work

y = 6
x = (1,2)

# create list

inventory = ("bike","worm-up pants","car","lunch" )

# print variable

print(y)
print(x)

print(inventory)
print(inventory[2])

# first loop

print("---> Regular loop")

count = 0

while count < 4:
    print(inventory[count])
    count = count + 1

# second loop

print("---> Backwards loop")

count = 3

while count < 0:
    print(inventory[count])
    count = count - 1

# for loop

print("---> the inventory for the loop")

for count in inventory:
    print(count)

