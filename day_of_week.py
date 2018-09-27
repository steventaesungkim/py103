#This helps you find out the days of the week with corresponding number (0-6).
#Sunday = 0, Monday = 1, Tuesday = 2, Wednesday = 3, Thursday = 4, Friday = 5, Saturday = 6

day = int(input("Find the day of the week using whole numbers(0-6)! "))

if day == 0:
    print("It is Sunday.")
elif day == 1:
    print("It is Monday.")
elif day == 2:
    print("It is Tuesday.")
elif day == 3:
    print("It is Wednesday.")
elif day == 4:
    print("It is Thursday.")
elif day == 5:
    print("It is Friday.")
elif day == 6:
    print("It is Saturday.")
else:
    print("Please try again. Enter a whole number between 0-6 to find the day of the week.")
print()


# days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# count = 0
# while count < day:
#     count += 1
# print(days_of_the_week[count])
# print()


    