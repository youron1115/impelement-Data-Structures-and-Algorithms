class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maximum=maxSize#最大容量
        self.top=0#目前量(以index表示)
        self.lists=[None]*self.maximum#需先將list填入none以免無法指定某index位置

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        if self.top<self.maximum:
            self.lists[self.top]=x
            self.top+=1
            
    def pop(self):
        """
        :rtype: int
        """
        if self.top>0:
            r=self.lists[self.top-1]#要pop並變為None的為lists[top]的前一個
            self.lists[self.top-1]=None
            self.top-=1
            return r
        else:
            return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        
        由下往上算，k個元素，將之加上val
        """
        for i in range(0,k):
            if i<len(self.lists) and self.lists[i]!=None:
                self.lists[i]+=val
            else:
                break 
        #print(self.lists)
        
