class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.limits = (big, medium, small)
        self.current = [0, 0, 0]
        
    def addCar(self, carType: int) -> bool:
        # make it 0-based
        carType -= 1 
        limit = self.limits[carType]
        current = self.current[carType]
        if limit > current:
            self.current[carType] += 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)