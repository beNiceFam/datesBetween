from datetime import date
import math

d1, m1, y1 = input("Enter the first date as DD MM YY: ").split()
d2, m2, y2 = input("And the second one too as DD MM YY: ").split()

firstDate = date(int(y1), int(m1), int(d1))
secondDate = date(int(y2), int(m2), int(d2))

totalSecs = abs((firstDate - secondDate).total_seconds())

print()
print(str(round(totalSecs)) + " seconds")
print(str(round(totalSecs/60)) + " minutes")
print(str(round(totalSecs/3600)) + " hours")
print(str(round(totalSecs/86400)) + " day(s)")

weeks = totalSecs/604800
daysRest = math.floor(((weeks % 1) * 7))

if weeks % 7 > 0 and weeks >= 1: 
    print(str(round(weeks)) + " week(s) and " + str(daysRest) + " day(s)")
elif weeks >= 1:
    print(str(round(weeks)) + " week(s)")

months = totalSecs/2592000
daysRest = math.floor(((months % 1) * 30))

if months % 30 > 0 and months >= 1:
    print(str(round(months)) + " month(s) and " + str(daysRest) + " day(s)")
elif months >= 1:
    print(str(round(months)) + " month(s)")
 
