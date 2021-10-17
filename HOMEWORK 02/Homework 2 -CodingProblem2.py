# Caleb Chan, 1831296
from datetime import datetime
from datetime import date


timeFormat = '%B %d %Y'  # establish strptime() format, %B for month, %d for day of month, %Y for XXXX year

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']  # LIST of Months

while True:  # Loop doesn't stop until userInput = -1
    userInput = input()
    if userInput == "-1":
        break

    try:
        dateValidity = bool(datetime.strptime(userInput, timeFormat))  # strptime() to
    except ValueError:
        dateValidity = False  # ignores unsuccessful dateValidity

    if dateValidity:  # for the successful dateValidity checks
        for monthNum in range(0, 12):
            if userInput.find(months[monthNum]) != -1:
                commaCheck = userInput.find(",")

                m = monthNum + 1  # gets month, +1 to account for range(0, 12)
                d = int(userInput[commaCheck-2:commaCheck].strip())
                y = int(userInput[-4:])

                trueDate = date(y, m, d)  # date(year, month, day) from the datetime module
                today = date.today()  # returns current local date, from datetime module
                dateComplete = str(m) + "/" + str(d) + "/" + str(y)

                print(dateComplete)
