from elevators import elevator


class building:
    def __init__(self, b):
        self.minfloor = b.get("_minFloor")
        self.maxfloor = b.get("_maxFloor")
        self.elevatorarr = []
        for e in b.get("_elevators"):
            self.elevatorarr.append(elevator(e))




# def __init__(self,elevators,elevators):
