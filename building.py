from Elevators import Elevators


class Building:
    def __init__(self, b):
        self.min_floor = b.get("_minFloor")
        self.max_floor = b.get("_maxFloor")
        self.elevator_arr = []
        for e in b.get("_elevators"):
            self.elevator_arr.append(Elevators(e))
