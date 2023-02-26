class double_end_heap :
    def __init__(self,array) :
        self.maxHeap = []; self.maxSize = 0;
        self.minHeap = []; self.minSize = 0;
        # [val , indexToAnother.]
        for i in array :
            self.insert(i)
        
        
    def insert(self,n) :
        
        self.maxHeap.append([n,self.maxSize])
        self.minHeap.append([n,self.minSize])
        

        self.__swim(self.maxSize,True)
        self.__swim(self.minSize,False)
        self.maxSize += 1
        self.minSize += 1


    def renewPoint(self,index,val,flag = False) :
        if flag :
            P = self.maxHeap[index][1]
            self.maxHeap[index][0] = val
            self.minHeap[self.maxHeap[index][1]][0] = val
        else :
            P = self.minHeap[index][1]
            self.minHeap[index][0] = val
            self.maxHeap[self.minHeap[index][1]][0] = val
        
        #print(self.maxHeap,self.minHeap,"P0")
        self.__swim(index,flag)
        #print(self.maxHeap,self.minHeap,"P0.5")
        self.__sink(index,flag)
        #print(self.maxHeap,self.minHeap,"P1")
        self.__swim(P,not flag)
        self.__sink(P,not flag)
        #print(self.maxHeap,self.minHeap,"P2",flag)
    def __swim(self,i,flag = False) :
        if flag :
            while i > 0 and self.maxHeap[i] > self.maxHeap[(i+1) // 2 - 1] :
                self.__swap(i,(i+1) // 2 - 1,True)
                i = (i+1) // 2 - 1
        else :
            while i > 0 and self.minHeap[i] < self.minHeap[(i+1) // 2 - 1] :
                self.__swap(i,(i+1) // 2 - 1,False)
                i = (i+1) // 2 - 1
    def __sink(self,i,flag = False) :
        if flag :
            while True :
                l,r = 2*i+1 ,2*i+2 
                mv,lv,rv = self.maxHeap[i][0],self.maxHeap[l][0] if l < self.maxSize else -float("inf"),\
                                            self.maxHeap[r][0] if r < self.maxSize else -float("inf")
                if mv < lv :
                    if lv >= rv :
                        self.__swap(i,l,True)
                        i = l
                    else :
                        self.__swap(i,r,True)
                        i = r
                elif mv < rv :
                    if rv >= lv :
                        self.__swap(i,r,True)
                        i = r
                    else :
                        self.__swap(i,l,True)
                        i = l
                else : break
        else :
            while True :
                l,r = 2*i+1 ,2*i+2 
                mv,lv,rv = self.minHeap[i][0],self.minHeap[l][0] if l < self.maxSize else float("inf"),\
                                              self.minHeap[r][0] if r < self.maxSize else float("inf")
                if mv > lv :
                    if lv <= rv :
                        self.__swap(i,l,False)
                        i = l
                    else :
                        self.__swap(i,r,False)
                        i = r
                elif mv > rv :
                    if rv <= lv :
                        self.__swap(i,r,False)
                        i = r
                    else :
                        self.__swap(i,l,False)
                        i = l
                else : break
    def __swap(self,a,b,flag = False) :

        if flag : 
            self.minHeap[self.maxHeap[a][1]][1] = b
            self.minHeap[self.maxHeap[b][1]][1] = a
            self.maxHeap[a],self.maxHeap[b] = self.maxHeap[b],self.maxHeap[a]
        else :
            self.maxHeap[self.minHeap[a][1]][1] = b
            self.maxHeap[self.minHeap[b][1]][1] = a
            self.minHeap[a],self.minHeap[b] = self.minHeap[b],self.minHeap[a]
