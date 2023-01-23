# Task 2.2


'''Step 1 - The computational issues consists of, that if the user is travelling at
            midnight the hours must reset to 0 and if he journey takes longer than 60 minutes the minutes would need to reset at 0. '''
departureTime = input("Please enter the departure time? Use format hh:mm")
departureHours, departureMinutes = int(departureTime[:2]), int(departureTime[3:5])

'''Step 2 - The data that needs to be stored is the departure time in the hh:mm form and the travel time in the hh:mm form.
            The algorithm will add the travel hours and minutes to the departure hourrs and minutes and check if hours is greater than 24
            or minutes is greater than 60 in which case it will reset to 0'''

travelJourney = input("Please enter the journey time? Use format hh:mm")
travelHours, travelMinutes = int(travelJourney[:2]), int(travelJourney[3:5])

arrivalHours = int(travelHours) + int(departureHours)
arrivalMinutes = int(travelMinutes) + int(departureMinutes)

'''Step 4 - Departure Time        Journey Time          Expected Time Of Arrival
               23:54             00:10 (10 mins)                00:04
               23:40             03:30 (3 hours 30 mins)        03:10
               13:01             28:50 (28 hours 10 mins)       17:11
               08:14             05:40 (5 hours 40 mins)        13:54     


'''
if arrivalMinutes > 59: 
    arrivalMinutes = arrivalMinutes - 60
    arrivalHours += 1

if arrivalHours > 23:
    arrivalHours = arrivalHours - 24
    
print("Your estimated time of arrival is %02d:%02d" % (arrivalHours, arrivalMinutes))
