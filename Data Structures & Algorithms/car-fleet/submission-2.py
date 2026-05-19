class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    

        # time = (target - position) / speed # time it takes for each car to arrive at target

        stack = []

        cars = sorted(zip(position, speed), reverse=True) 
        print(cars)
        car_fleet = 0
        for p, s in cars: 

            t = (target - p) / s 

            print(t)

            if not stack: 

                stack.append(t) 
                car_fleet += 1

            elif t not in stack:
                prev_time = stack[-1]

                if t >= prev_time: 
                    stack.append(t) 
                    car_fleet += 1

                

        return car_fleet