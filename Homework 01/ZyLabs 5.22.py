# Hero Chan, 1831296

print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12")

# total cost dictionary
serviceCost = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12, "-": 0}


service1 = input('\nSelect first service:\n')
service2 = input('Select second service:\n')

print("\nDavy's auto shop invoice\n")

if service1 == "-":
    print('Service 1: No service')
else:
    print('Service 1: {}, ${}'.format(service1, serviceCost.get(service1)))

if service2 == "-":
    print("Service 2: No service")

else:
    print("Service 2: {}, ${}".format(service2, serviceCost.get(service2)))

total = serviceCost.get(service1) + serviceCost.get(service2)
print("\nTotal: ${}".format(total))
