
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        
        初始五件事:size of k/queue/front/rear/length
        """
        self.k=k#the size of the queue to be k
        self.queue=[None]*self.k
        self.f=0
        self.r=0
        self.length=0#塞多少東西了
        """
        print("k:",self.k)
        print("queue:",self.queue)
        print("f:",self.f)
        print("r:",self.r)
        """
        
    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue[self.r]=value
            self.r = (self.r + 1) % self.k
            self.length+=1
            return True
        else:
            return False
        
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty(): 
            self.queue[self.f]=None
            self.f = (self.f + 1) % self.k
            self.length-=1
            return True
        else:
            return False
    
    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.f]
        
    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.r-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return  self.length == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        
        return  self.length == self.k  

