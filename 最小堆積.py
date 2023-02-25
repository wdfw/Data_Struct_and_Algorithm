class heap :
    def __init__(self,element) :
        self.heap = []
        for i in element :
            self.insert(i)
        
    def insert(self,n) :
        self.heap.append(n)
        i = len(self.heap)-1
        while i > 0 and self.heap[i] < self.heap[(i-1)//2]:
            self.__swap(i,(i-1)//2)
            i = (i-1) // 2
            
    def pop(self) :
        self.__swap(0,-1) 
        res = self.heap.pop()
        self.__sink(0)
        return res
    
    def __sink(self,i) :
        while i*2+1 < len(self.heap) :
            v = i*2 + 1
            if v+1  < len(self.heap) and self.heap[v+1] < self.heap[v] : v+=1
            self.__swap(i,v)
            i = v
            
    def __swap(self,i,j) :
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
        
a = heap([7,3,2,6])
print(a.pop(),a.heap)


        
