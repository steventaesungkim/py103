#Tip Calculator
#You will be able to calculate the tip and the total amount according to the level of service received.

sub_amount = float(input("How much was your meal? "))
service = str(input("How was your service? Pick one: Good, Fair, or Bad. "))

service_Good = 1.20 * sub_amount
service_Fair = 1.15 * sub_amount
service_Bad = 1.10 * sub_amount

tip_Good = 0.20 * sub_amount
tip_Fair = 0.15 * sub_amount
tip_Bad = 0.10 * sub_amount

if service.upper() == "GOOD":
    print (("The tip amount of Good is: %.02f.") % (tip_Good))
    print (("The total amount of your meal with tip is: %.02f.") %(service_Good))
elif service.upper() == "FAIR":
    print (("The tip amount of Fair is: %.02f.") % (tip_Fair))
    print (("The total amount of your meal with tip is: %.02f.") %(service_Fair))
elif service.upper() == "BAD":
    print (("The tip amount of Bad is: %.02f.") % (tip_Bad))
    print (("The total amount of your meal with tip is: %.02f.") %(service_Bad))
else:
    print("Please try again. Enter in the amount of your meal and how your service was: Good, Fair, Bad.")
