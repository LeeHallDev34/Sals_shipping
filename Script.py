weightInput = input("Enter package weight in lbs ")

weight = float(weightInput)


#Ground Shipping

gs = "Ground Shipping"
gFlat_Charge = 20.00

if weight <= 2:
  print(gs,weight * 1.50 + gFlat_Charge)
elif weight <= 6:
  print(gs,weight * 3.00 + gFlat_Charge)
elif weight <= 10:
  print(gs,weight * 4.00 + gFlat_Charge)
else:
  print(gs,weight * 4.75 + gFlat_Charge)

#Premium Ground Shipping
pre_ground_shipping = 125.00
print("Premium Ground Shipping",pre_ground_shipping)

#Drone Shipping

ds = "Drone Shipping"

if weight <= 2:
  print(ds,weight * 4.50)
elif weight <= 6:
  print(ds,weight * 9.00)
elif weight <= 10:
  print(ds,weight * 12.00)
else:
  print(ds,weight * 14.25)




