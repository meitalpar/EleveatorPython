# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from building import building
from elevators import elevator
import json
import csv
import shutil


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
buildingname = input()
callsname=input()
output=input()



with open(buildingname) as f:
#with open('B3.json') as f:
#with open(r'C:\Users\meita\OneDrive\Desktop\building\B3.json') as f:
 data = json.load(f)
 b = building(data)

#print(data.get("_elevators")[0].get("id"))
# Iterating through the json
# list

# Closing file
f.close()


def well (b:building,src:int,des:int):
    timem =b.elevatorarr[0].time(src,des)+b.elevatorarr[0].Time
    ans = b.elevatorarr[0]
    index = 0
    iii=0
    upordown = 2
    if (des>src):
        upordown= 1
    else:
        upordown= -1



    for i in b.elevatorarr:
        timei =i.time(src,des)
        if ( (timei+i.Time)<timem ):
            iii=index
            ans = i
            timem = timei+i.Time
                    #+i.time(last,src)
        index=index+1
    if(ans!=0):
        ans.Time=(ans.Time+timem)
    print('iii',iii)
    return iii





with open(callsname) as in_file:
    reader = csv.reader(in_file)
    with open(output,'w', newline='') as out_file:

        writer = csv.writer(out_file)

        for row in reader:
            src = int(row[2])
            des = int(row[3])
            row[5] = (well(b, src, des))
            writer.writerow(row)

in_file.close()
out_file.close()








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
