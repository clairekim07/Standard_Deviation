import csv
import math
totalSum = 0
with open("std.csv", newline='') as std:
    read = csv.reader(std)
    newData = list(read)
    length = len(newData)

    for num in newData:
        totalSum += int(num)
        mean = totalSum/length

        standard = ((num-mean)**2)/length
        stdev = math.sqrt(standard)
        print("The standard deviation is:" + str(stdev))
