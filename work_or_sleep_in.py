#This helps you find out what days we have to go to work and when we can sleep in with the corresponding number (0-6).
#Sunday = 0, Monday = 1, Tuesday = 2, Wednesday = 3, Thursday = 4, Friday = 5, Saturday = 6

day = int(input("Enter in a whole number to find out if you have to go to work or sleep in (0-6)! "))

if 1 <= day <= 5:
    print("Go to work! NOW!")
elif 0 == day or day == 6:
    print("Please sleep in! ZZz!")
else:
    print("Please try again. Enter a whole number between 0-6 to see if you have to go to work or sleep in.")
print()