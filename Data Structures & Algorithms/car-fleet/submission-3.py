class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    

        # time = (target - position) / speed # time it takes for each car to arrive at target

        stack = []
        cars = sorted(zip(position, speed), reverse=True) 
        for p, s in cars: 

            t = (target - p) / s 

            if not stack or t > stack[-1]: 

                stack.append(t) 

                

        return len(stack)