#Quiz Question

answer = input("What is the capital of France?\n")
answer = answer.title()  #A method to change answer to Title case

while answer != "Paris":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
print("Correct! Well done.")

input("\n\nPress ENTER to exit") # \n means new line is the code equivalent of pressing enter 



# what title case is 
"""title case is something not often used what it does is changes the
string saved as the variable answer into a title e.g. in this code
answer.title() Paris or Milan or whatever city the user types as there answer
but only Paris is correct"""
