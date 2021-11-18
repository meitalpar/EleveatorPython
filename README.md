# ElevatorPython
In this task an offline algorithm is opened for an elevator system and the amount of a high-rise building. That is, all the calls are given to us in advance, and we only have to insert a call to the elevator.

Sources of information:

https://www.youtube.com/watch?v=xOayymoIl8U

https://www.youtube.com/watch?v=siqiJAJWUVg

https://blackswanfarming.com/scheduling-algorithms-elevator-edition

https://elevation.fandom.com/wiki/Elevator_algorithm



# Our offline algorithm:
The idea:

We allocated different calls to different elevators considering the time it takes for each elevator to perform the call, and taking in to consideration the time it took for each elevator to perform her previous allocated calls 

The algorithm:

The input was json and csv files of buildings and calls.
We built classes of buildings and elevators and We defined variables according to the inputs.
We added a field and function of times and checked for each call which elevator have the fastest execution time for that call and we assigned it to this call.
We did this using a loop that goes through elevator_arr and check the time.





