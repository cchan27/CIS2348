# Hero Chan, 1831296

wallHeight = int(input('Enter wall height (feet):\n'))
wallWidth = int(input('Enter wall width (feet):\n'))
gallonSquareFt = float(350)

# dictionary: red 35, blue 75, green 23
paintCost = {"red": "$35", "blue": "$75", "green": "$23"}

print('Wall area: {} square feet'.format(wallHeight * wallWidth))
print('Paint needed: {:.2f} gallons'.format(wallHeight * wallWidth / gallonSquareFt))
print('Cans needed: {} can(s)'.format(round(wallHeight * wallWidth / gallonSquareFt)))

paintColor = input('\nChoose a color to paint the wall:\n')
print('Cost of purchasing', paintColor, 'paint:', paintCost[paintColor])

