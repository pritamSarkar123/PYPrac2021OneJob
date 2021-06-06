import heapq 
class MyHeap:
    def __init__(self,items=None,key = lambda x: x):
        self.__heap_list = []
        self.__heap_index = 0
        self.__heap_key = key
        if items:
            self.__heap_list = [(self.__heap_key(x),i,x) for i,x in enumerate(items)]
            self.__heap_index = len(self.__heap_list)
            heapq.heapify(self.__heap_list)
    def push(self,item):
        heapq.heappush((self.__heap_key(item),self.__heap_index,item))
        self.__heap_index += 1
    def pop(self):
        return heapq.heappop(self.__heap_list)[-1]
    def size(self):
        return len(self.__heap_list)
    def show(self):
        for item in self.__heap_list:
            print(item[-1],end = " ")
        print()

if __name__ == '__main__':
    l =[[0,30],[15,20],[5,10]]
    heap = MyHeap(l,key = lambda x:-(x[0]*x[0]+x[1]*x[1]))
    print(type(heap),heap)
    heap.show()
    while heap.size():
        print(heap.pop())



