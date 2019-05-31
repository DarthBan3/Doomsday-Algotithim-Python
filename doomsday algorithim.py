#RANDOM COMMENT THAT MAKES ME REALISE CAPS LOCK IS ON
#Random comment to test caps lock off

obiwan = 25
if obiwan==25:
    print ("Hello There!")
else:
    print ("Did you really think I would leave the hyperdrive unguarded")

date = int(input("Date"))
month = int(input("Month Number"))
year = int(input("Year"))

y_rem = year%400
print (y_rem, "is the remainder after dividing by 400")

if y_rem < 100:
    century_code = 2
elif y_rem >= 300:
    century_code = 3
elif y_rem >= 200:
    century_code = 5
elif y_rem >= 100:
    century_code = 0



print ("Century Code is", century_code)

digit1 = year%100
print ("Last 2 digits are:", digit1)

rem1 = digit1%12
digit2 = (digit1 - rem1)/12
digit3 = (rem1 - rem1%4)/4
print (rem1, digit2, digit3)
sigma = rem1 + digit2 + digit3 + century_code
print (sigma)

if month == 1:
    if year%4 == 0:
        doomsday = 4
    else:
        doomsday = 3
elif month == 2:
    if year%4 == 0:
        doomsday = 29
    else:
        doomsday = 28
elif month == 3:
    doomsday = 14
elif month == 4:
    doomsday = 4
elif month == 5:
    doomsday = 9
elif month == 6:
    doomsday = 6
elif month == 7:
    doomsday = 11
elif month == 8:
    doomsday = 8
elif month == 9:
    doomsday = 5
elif month == 10:
    doomsday = 10
elif month == 11:
    doomsday = 7
elif month == 12:
    doomsday = 12
print ("doomsday for given month is", doomsday)

no_of_days = date - doomsday
print ("The date is ", no_of_days, " days away from the doomsday")

final = (no_of_days + sigma)%7

if final == 0:
    print ("The day is a sunday")
elif final == 1:
    print ("The day is a monday")
elif final == 2:
    print ("The day is a tuesday")
elif final == 4:
    print ("The day is a thursday")
elif final == 3:
    print ("The day is a wednesday")
elif final == 5:
    print ("The day is a friday")
elif final == 6:
    print ("The Day is a Saturday")
