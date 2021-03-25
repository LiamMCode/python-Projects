
metre_start = input("enter metre reading at start of the month")
metre_end = input("enter the metre reading at the end of the month")
price_per_unit = input("what is the price per unit of electricity")

number_of_units = float(metre_end) - float(metre_start)
cost = float(number_of_units) * float(price_per_unit)
print (cost)
