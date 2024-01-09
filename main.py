# Odd or Even program
# even numbers can be divided by 2 with no remainder otherwise is an odd number.
# % it gives u the remainder after a division.


# which number do u wanna check?
number = int(input("Enter the number: "))

if (number % 2 == 0):
  print(f"{number} is an even number.")
else:
  print(f"{number} is an odd number.")