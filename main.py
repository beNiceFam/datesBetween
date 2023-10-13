from datetime import date, timedelta

d1, m1, y1 = input("Enter the first date as DD MM YY: ").split()
d2, m2, y2 = input("And the second one too as DD MM YY: ").split()

firstDate = date(int(y1), int(m1), int(d1))
secondDate = date(int(y2), int(m2), int(d2))

seconds = abs((firstDate - secondDate).total_seconds())

print(str(seconds) + " seconds")
print(str(seconds/60) + " minutes")
print(str(seconds/3600) + " hours")
print(str(seconds/86400) + " days")
print(str(seconds/604800) + " weeks")
