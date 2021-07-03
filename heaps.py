class Minheap:
    def __init__(self,array):
        self.heap = array
        self.size = len(array)
        self.buildHeap()

    def parent(self,i):
        if i % 2 == 0:
            return int((i - 2)/2)
        else:
             return int((i-1)/2)

    def heapifyDown(self,index):
        i = int(index)
        smallest = i
        l = int(2*i + 1)
        r = int(2*i + 2)

        if (l <= self.size-1 and self.heap[l] < self.heap[smallest]) :
            smallest = l
        if (r <= self.size-1 and self.heap[r] < self.heap[smallest]) :
            smallest = r

        if (smallest != i):
            temp = self.heap[i]
            self.heap[i] = self.heap[smallest]
            self.heap[smallest] = temp
            self.heapifyDown(smallest)
    
    def buildHeap(self):
        i = int(self.size/2)
        while i >= 0:
            self.heapifyDown(i)
            i-=1

    def getTop(self):
        res = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.size -=1
        self.heapifyDown(0)

        return res

    def heapifyUp(self,i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            temp = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = self.heap[i]
            self.heap[i] = temp
            i = self.parent(i)

    def add(self,item):
        self.size +=1
        self.heap.append(item)
        self.heapifyUp(self.size-1)


# by all means take control
class MaxHeap:
    def __init__(self,array):
        self.heap = array
        self.size = len(array)
        self.buildHeap()

    def parent(self,i):
        if i % 2 == 0:
            return int((i - 2)/2)
        else:
             return int((i-1)/2)

    def heapifyDown(self,index):
        i = int(index)
        largest = i
        l = int(2*i + 1)
        r = int(2*i + 2)

        if (l <= self.size-1 and self.heap[l] > self.heap[largest]) :
            largest = l
        if (r <= self.size-1 and self.heap[r] > self.heap[largest]) :
            largest = r

        if (largest != i):
            temp = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = temp
            self.heapifyDown(largest)
    
    def buildHeap(self):
        i = int(self.size/2)
        while i >= 0:
            self.heapifyDown(i)
            i-=1

    def getTop(self):
        res = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.size -=1
        self.heapifyDown(0)

        return res

    def heapifyUp(self,i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            temp = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = self.heap[i]
            self.heap[i] = temp
            i = self.parent(i)

    def add(self,item):
        self.size +=1
        self.heap.append(item)
        self.heapifyUp(self.size-1)


        


            



        





        