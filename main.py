from datetime import date, timedelta

d1, m1, y1 = input("Enter the first date as DD MM YY: ").split()
d2, m2, y2 = input("And the second one too as DD MM YY: ").split()

firstDate = date(int(y1), int(m1), int(d1))
secondDate = date(int(y2), int(m2), int(d2))

between = abs((firstDate - secondDate).total_seconds())

print("The amount of days is: " + str(between/86400))