
month = input("Enter the month of year:")

#variable.title() converts to title case with capital first letter
month = month.title()

if month == "December" or month == "January" or month == "February":
    print(month,"is in Winter")
elif month == "March" or month == "April" or month == "May":
    print(month,"is in Spring")
elif month == "June" or month == "July" or month == "August":
    print(month,"is in Summer")
elif month == "September" or month == "October" or month == "November":
    print(month,"is in Autumn")
else:
    print("Check spelling of month.")
    
input("Press ENTER to quit")
