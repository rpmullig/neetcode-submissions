class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count: int = 0
        sorted_cars = []
        for i in range(len(position)):
            sorted_cars.append((position[i], speed[i]))

        sorted_cars.sort(key=lambda x: -x[0])
        stack = []

        for car in sorted_cars:
            pos, speed = car
            while stack and stack[-1] < (target - pos) / speed:
                stack.pop()
            
            if len(stack) == 0:
                fleet_count += 1
            stack.append((target - pos) / speed)
            print(stack)

        return fleet_count