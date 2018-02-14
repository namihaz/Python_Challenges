import datetime

name = input("What is you name? \n")
age = int(input("What is your age? \n"))

Year = int(datetime.date.today().strftime("%Y"))

# Year when you will turn 100    
yr_later = Year + (100 - age)

copynum = name + " will be 100 years old in the year " + str(yr_later) + '\n'
msg = int(input("Please enter the number of messages you want: " ))

print(copynum * msg)

input("Press enter to exit.")
 
