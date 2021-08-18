# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands, obstacles):
        obs = set([tuple(x) for x in obstacles])
        obs.remove((0,0))
        print(obs)
        m2 = {
            "n":["w","e"],
            "s":["e","w"],
            "e":["n","s"],
            "w":["s","n"]
        }
        point = [0,0]
        d = "n"
        for c in commands:
            print(d)
            if 1<=c<=9:
                command = c
                if d == "n":                
                    while tuple(point) not in obs and command:
                        point[1] += 1
                        command -=1
                    while tuple(point) in obs:
                        point[1]-=1
                    print(point)
                elif d == "s":                
                    while tuple(point) not in obs and command:
                        point[1] -= 1
                        command -=1
                    while tuple(point) in obs:
                        point[1] +=1
                    print(point)
                elif d == "e":                
                    while tuple(point) not in obs and command:
                        point[0] += 1
                        command -=1
                    while tuple(point) in obs:
                        point[0]-=1
                    print(point)
                else:            
                    while tuple(point) not in obs and command:
                        point[0] -= 1
                        command -=1
                    while tuple(point) in obs:
                        print(f"ffffff {point}")
                        point[0] +=1   
                    print(point)
            elif c == -1 or c==-2:
                d = m2[d][c]
            
        return point[0]*point[0] + point[1]*point[1]
                
if __name__ =="__main__":
    s=Solution()
    a = [-2,-1,-2,3,7]
    b = [[1,-3],[2,-3],[4,0],[-2,5],[-5,2],[0,0],[4,-4],[-2,-5],[-1,-2],[0,2]]
    print(s.robotSim(a,b))    