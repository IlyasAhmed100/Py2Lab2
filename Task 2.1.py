# Task 2.1

#List Containing Weekdays
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#Printing The Weekdays
print(weekdays)

#Printing Second Entry Of List
print(weekdays[1])

#Updating Last Entry To 'My favourite day'
weekdays[-1] = "My favourite day"
print(weekdays)

#Deleting Second, Third And Forth Entries And Replacing With "Some more days"
del weekdays[3]
del weekdays[2]
del weekdays[1]
weekdays.insert(1,"Some more days")
print(weekdays)
