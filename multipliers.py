#!/usr/bin/env python3

from math import log

# for simple and compound interest and stuff but made the names sound like it could be used for other stuff too without getting confused

def findResult(times, by, compounding, startValue, endValue):
    times = int(times)
    by = float(by)
    startValue = float(startValue)
    endValue = float(endValue)
    
    if compounding == "c":
        compounding = True
    else:
        compounding = False
    
    if compounding:
        if startValue > 0 and by > 0 and times > 0:
            endValue = startValue * by**times
        
        elif endValue > 0 and by > 0 and times > 0:
            startValue = endValue / (by**times)
        
        if times == 0 and startValue > 0 and endValue > 0 and by > 0:
            times = log(endValue/startValue)/log(by)

        if by == 0 and startValue > 0 and endValue > 0 and times > 0:
            by = (endValue/startValue)**(1/times)
    

    elif not compounding:
        if startValue > 0 and times > 0 and by > 0:
            endValue = startValue * (1 + (times * (by - 1)))
            
        elif endValue > 0 and times > 0 and by > 0:
            startValue = endValue / (1 + (times * (by - 1)))

        if times == 0 and startValue > 0 and endValue > 0 and by > 0:
            times = ((endValue/startValue) - 1) / (by - 1)

        if by == 0 and startValue > 0 and endValue > 0 and times > 0:
            by = (((endValue/startValue) - 1) / times) + 1
            
        
    return [startValue, endValue, times, by]
    

timesMultiplied = 0
multipliedBy = 0
startValue = 0
endValue = 0
ready = False

print("(C)ompounding - (S)imple")
compoundingOrElse = input("┃ ").lower()

while not ready:
    print("\n" + "(S)tart value - (E)nd Value - (T)imes - (M)ultiplied by - (Q)uit")
    TorMorV = input("┃ ").lower()
    print("\n")
    
    if TorMorV == "t":
        print(".. has been multiplied 𝑥 times ..")
        timesMultiplied = input("┃ ")
    
    elif TorMorV == "m":
        print(".. has been multiplied by 𝑥 ..")
        multipliedBy = input("┃ ")
    
    elif TorMorV == "s":
        print(".. value started as x ..")
        startValue = input("┃ ")
    
    elif TorMorV == "e":
        print(".. value ended as x ..")
        endValue = input("┃ ")

    elif TorMorV == "q":
        ready = True

listResults = findResult(timesMultiplied, multipliedBy, compoundingOrElse, startValue, endValue)

startValue = listResults[0]
endValue = listResults[1]
timesMultiplied = listResults[2]
multipliedBy = listResults[3]

print("\n" + f"Start value ┃ {startValue}")
print(f"End value   ┃ {endValue}")
print(f"Times       ┃ {timesMultiplied}")
print(f"By          ┃ {multipliedBy}")
