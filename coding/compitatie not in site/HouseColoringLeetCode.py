# https://www.youtube.com/watch?v=fZIsEPhSBgM&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=18
from functools import reduce
def colorHouses(prices,noOfHouses):
    cost=[float('inf')]*(noOfHouses)
    colors=[0,1,2]
    ignore_color=-1
    for i in range(noOfHouses):
        for j in range(3):
            if j!= ignore_color:
                if prices[i][j] < cost[i]:
                    ignore_color = j 
                    cost[i]= prices[i][j]
    return reduce(lambda x,y:x+y,cost)
                
if __name__=="__main__":
    prices= [[17,2,17],[16,16,5],[14,3,19]]
    noOfHouses=3
    print(colorHouses(prices,noOfHouses))