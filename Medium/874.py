"""
Walking Robot Simulation (Medium)
Solved in O(n * m) time complexity and O(m) space complexity where m is the number of obstacles
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        idx = 0
        check = {}
        for obs in obstacles:
            check[tuple(obs)] = None
        output = 0

        print(check)

        for command in commands:
            if command == -2:
                idx = (idx - 1) % 4
            elif command == -1:
                idx = (idx + 1) % 4
            else:
                print(command)
                for _ in range(command):
                    if ((x+directions[idx][0], y+directions[idx][1]) in check):
                        # hit obstacle
                        break
                    x += directions[idx][0]
                    y += directions[idx][1]
                    output = max(output, (x*x) + (y*y))
        return output