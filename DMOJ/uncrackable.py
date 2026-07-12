# Read the password string from input
password = input().strip()


# Initialize counters for each type of character
lowercase = 0
uppercase = 0
digits = 0


# Count how many of each type are in the password
for char in password:
   if char.islower():    # If the character is lowercase
       lowercase += 1
   elif char.isupper():  # If the character is uppercase
       uppercase += 1
   elif char.isdigit():  # If the character is a digit
       digits += 1


# Check if all  requirements are satisfied
if 8 <= len(password) <= 12 and lowercase >= 3 and uppercase >= 2 and digits >= 1:
   print("Valid")
else:
   print("Invalid")
