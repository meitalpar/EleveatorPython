# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from building import building
from elevators import elevator
from callsfromfile import savecalls
import json
import csv
import shutil
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


buildingname = input()
callsname = input()
output = input()

with open(buildingname) as f:
    # with open('B3.json') as f:
    # with open(r'C:\Users\meita\OneDrive\Desktop\building\B3.json') as f:
    data = json.load(f)
    b = building(data)

# print(data.get("_elevators")[0].get("id"))
# Iterating through the json
# list

# Closing file
f.close()


def well(b: building, src: int, des: int):
    timem = b.elevatorarr[0].time(src, des) + b.elevatorarr[0].Time
    ans = b.elevatorarr[0]
    index = 0
    iii = 0
    for i in b.elevatorarr:
        timei = i.time(src, des)
        if ((timei + i.Time) < timem):
            iii = index
            ans = i
            timem = timei + i.Time + i.time(i.destination, src)
        index = index + 1
    if (ans != 0):
        ans.Time = (ans.Time + timem + i.time(i.destination, src))
        print('anstime',ans.Time)
        ans.destination = des
    print('iii', iii)

    return iii


def update(b: building,index,src,des):
    num = 0
    for j in b.elevatorarr:
        if (num==index):
           j.Time= j.Time+j.time(src,des)
           j.destination = des
           print('upppddate')
        num = num +1




# timearray = []
with open(callsname) as in_file:
    reader = csv.reader(in_file)
    time = 0
    lastsrc = 0
    with open(output, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        lasttindex = 0
        upordown = 2
        lastupordown = 0
        for row in reader:
            src = int(row[2])
            des = int(row[3])
            if (des > src):
                upordown = 1
            else:
                upordown = -1
            print('time',time)
            ttt = 0
            if ((upordown == 1) and (lastsrc<=src))or (upordown == -1 and (lastsrc>=src) ):
                ttt = 1
            if ((time != 0) and (float(row[1]) - time < 10) and (upordown == lastupordown) and (ttt==1)):
                    row[5] = lasttindex
                    update(b,lasttindex,src,des)
                    print('iwentif')

            else:
                    row[5] = (well(b, src, des))
                    print('iwantintoelse')
                    lasttindex = row[5]
            print('row5',row[5])
            time = float(row[1])
            for e in b.elevatorarr:
                print(e.Time)
            lastsrc = src
            print('lstupdown',lastupordown)
            lastupordown = upordown
            writer.writerow(row)

in_file.close()
out_file.close()
# print(timearray)


print('6')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
