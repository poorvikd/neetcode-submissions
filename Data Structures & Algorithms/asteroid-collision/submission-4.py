class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for curr in asteroids:
            alive = True
            while alive and stack and curr < 0 and stack[-1] > 0:
                if abs(curr) > stack[-1]:
                    stack.pop(-1)
                elif abs(curr) < stack[-1]:
                    alive = False
                else:
                    stack.pop(-1)
                    alive = False
            if alive:
                stack.append(curr)
                
       
        
        return stack