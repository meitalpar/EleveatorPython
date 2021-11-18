import os

from building import Building
from Elevators import Elevators
import json
import csv
os.remove("hy.csv")
building_name = "B5.json"
calls_name = "calls_d.csv"
output = "hy.csv"
# receive 3 inputs:
# building_name = input()
# calls_name = input()
# output = input()

# read from json file
with open(building_name) as f:
    data = json.load(f)
    b = Building(data)


# A function that will assign to the call the  elevator whose time to perform that call is the fastest.
def allocate(b: Building, src: int, des: int):

    the_best_time = b.elevator_arr[0].time(src, des) + b.elevator_arr[0].Time+ b.elevator_arr[0].time(b.elevator_arr[0].destination, src)
    ans = b.elevator_arr[0]
    index = 0
    correct_index = 0

    for i in b.elevator_arr:
        comparison_time = i.time(src, des)
        if (comparison_time + i.Time) < the_best_time:
            correct_index = index
            ans = i
            the_best_time = comparison_time + i.Time + i.time(i.destination, src)
        index = index + 1
    ans.Time = ans.Time + ans.time(src,des)+ ans.time(ans.destination, src)
    ans.destination = des

    return correct_index


# read from csv file and write to another
with open(calls_name) as in_file:
    reader = csv.reader(in_file)
    with open(output, 'w', newline='') as out_file:
        writer = csv.writer(out_file)

        for row in reader:
            src = int(row[2])
            des = int(row[3])
            # function call and inlay in column 5
            row[5] = (allocate(b, src, des))
            writer.writerow(row)