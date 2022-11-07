import math
import numpy
from colorama import Fore
from colorama import Style

targetTime = 216

def parseTime(timeString):
    split = str.split(timeString, ":")
    return int(split[0])*60 + int(split[1])

class Plane:

    def getTime(self, index):
        split = str.split(self.speedString, " ")
        if (index*3+2<len(split)):
            return parseTime(split[index*3+2])
        else:
            return targetTime

    def parseSpeedString(self):
        speeds = []
        times = []
        distances = []
        split = str.split(self.speedString, " ")

        for i in range(int(len(split)/3)):
            newSpeed = int(split[i*3])
            timeDif = self.getTime(i+1)-self.getTime(i)
            speeds.append(newSpeed)
            times.append(timeDif)
            distances.append(timeDif / 3600 * newSpeed)

        return speeds, times, distances


    def __init__(self, color, name, ModDistance, speedString):
        self.color = color
        self.name = name
        self.speedString = speedString
        self.ModDistance = ModDistance

    def calcModDiff(self):
        distanceTraveled = 0
        speeds, times, distances = self.parseSpeedString()
        for i in range(len(distances)):
            distanceTraveled += distances[i]

        return abs(self.ModDistance-distanceTraveled)

def strSpeed(speed):
    return str(speed) + "kts"

def strTime(time):
    mins = math.floor(time/60)
    secs = time%60

    if (secs < 10):
        secs = "0"+str(secs)
    else:
        secs = str(secs)

    return str(mins)+":"+secs

def getProof(planes):
    # Initial Display
    for i in range(len(planes)):
        plane = planes[i]

        speeds, times, distances = plane.parseSpeedString()

        print(f"{plane.color}{plane.name}:")
        print("Distance to the reference point is "+str(plane.ModDistance)+"nm")

        routeOutput = "Starting at "+strSpeed(speeds[0])
        for j in range(1, len(speeds)):
            routeOutput += ", then at " + strTime(times[j]) + " changes to " + strSpeed(speeds[j])

        print(routeOutput)

        # Distance calc

        def getCalcString(j):
            final = f"{distances[j]:.2f}"
            return str(speeds[j]) + " * ("+str(plane.getTime(j+1)) + " - " + str(plane.getTime(j)) + ") / 3600 = " + final

        print("Calculation Distance Travelled: ")
        print(getCalcString(0))
        for j in range(1, len(distances)):
            print(" + "+getCalcString(j))
        print(" = {:.2f}nm".format(numpy.sum(distances)))
        print("Distance from reference point = | {:.2f}nm - {:.2f}nm | = {:.2f}nm".format(numpy.sum(distances), 
        plane.ModDistance, plane.calcModDiff()))
        print(Style.RESET_ALL)

    # Compare Distance
    print()
    print("Comparing Distances")
    for i in range(len(planes)-1):
        p1 = planes[i]
        for j in range(i+1, len(planes)):
            p2 = planes[j]
            p1Dif = p1.calcModDiff()
            p2Dif = p2.calcModDiff()
            part1 = f"{p1.color}{p1.name}{Style.RESET_ALL} to {p2.color}{p2.name}{Style.RESET_ALL}"
            part2 = f" = | {p1.color}{p1Dif:.2f}nm{Style.RESET_ALL} - {p2.color}{p2Dif:.2f}nm {Style.RESET_ALL}| = {abs(p1Dif - p2Dif):.2f}nm"
            print(f"{part1}{part2}")

bluePlane = Plane(Fore.BLUE, "Red AAL12", 32, "600 at 0:0")
greenPlane = Plane(Fore.GREEN, "Green DAL88", 35, "600 at 0:0")
redPlane = Plane(Fore.RED, "Blue UAL74", 38, "600 at 0:0")
targetTime = 3*60 + 36

# print(redPlane.calcModDiff())
getProof([redPlane, bluePlane, greenPlane])