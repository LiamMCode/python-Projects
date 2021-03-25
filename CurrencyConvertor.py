Amount = float
(input("Enter conversion amount in pounds: "))
Currency = input("Press 1 for Indian Rupees, 2 for Chinese Yuan or 0 to exit: ")

if Currency == "1":
    Amount = Amount * 100
    print ("You will get",Amount,"Indian Rupees")
elif Currency == "2":
    Amount = Amount * 10
    print ("You will get",Amount,"Chinese Yuan")
else:
    print ("Goodbye")

