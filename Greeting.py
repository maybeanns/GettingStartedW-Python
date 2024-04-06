import time
timehour = int(time.strftime('%H'))
timestamp = time.strftime('%H:%M:%S %p')
print("Good", end=" ")
if (timehour>=20 and timehour<=5):
    print("Night",end=", Sir")
elif(timehour>=13 and timehour<=19):
    print("Afternoon", end=", Sir")
else:
    print("Morning", end=", Sir")    
    
print("\nThe time is: ",timestamp)

    