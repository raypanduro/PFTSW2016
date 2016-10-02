#import the random module
import random
#random.seed(1)
down = None
up1 = None
up2 = None

#Set your starting coordinates
latPosition = 33.8091703
longPosition = -117.927007

#Open a file to write into
f = open('gpstest.txt', 'w')
f.write('type,latitude,longitude\n')
f.write("T," + str(latPosition) + "," +
str(longPosition) + "\n")

#A for loop to repeat X times
for i in range (0, 50):
    rup = random.randint(0,3)
    #Random choice: Up/Down, Left/Right?
    if rup == 1:
        up1 = True
        up2 = True
    elif rup == 2:
        up1 = False
        up2 = False
    elif rup == 3:
        up1 = True
        up2 = False
    else:
        up1 = False
        up2 = True
    #Random difference: What difference in lat/long pos?
    upDiff = random.random() * 9

    #Latitude
    if up1 == True:
        latPosition += upDiff
    else:
        latPosition -= upDiff

    #The same for Longitude
    if up2 == True:
        longPosition += upDiff
    else:
        longPosition -= upDiff

    #Write into the file
    f.write("T," + str(latPosition) + "," +
str(longPosition) + "\n")
#Close the file to behave nicely

f.close()
