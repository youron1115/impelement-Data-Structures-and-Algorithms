class Node_tree:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None
        #self.left_parent=None#左子節點的父節點，即自己在父節點的左邊
        #self.right_parent=None#右子節點的父節點，即自己在父節點的右邊
       
class BST():
    def __init__(self,root=None):#初始化
        self.root=root
        
    def insert(self,value=None):#插入節點
        if self.root==None:
            print("樹中無內容\n======================")
            self.root=Node_tree(value)
            #print("root:",self.root.value)
        else:
            self.__insert(value,self.root)
            
    def  __insert(self,value,cur_value):
        #print("value:",value)
        #print("cur_value:",cur_value.value,"\n=======================")
        if value<cur_value.value:
            #print("執行左邊")
            if cur_value.left:
                self.__insert(value,cur_value.left)
            else:
                cur_value.left=Node_tree(value)
                cur_value.left.parent=cur_value
        elif value>cur_value.value:
            #print("執行右邊")
            if cur_value.right:
                self.__insert(value,cur_value.right)
            else:
                cur_value.right=Node_tree(value)
                cur_value.right.parent=cur_value
        """
        else:
            print("執行else,已存在")
        """
        
    def delete(self,value):
        print("刪除:",value)
        if self.root!=None:
            self.__delete(value,self.root)
            
    
    def __delete(self,value,cur_value):
        if value<cur_value.value:
            if cur_value.left:
                self.__delete(value,cur_value.left)
            else:
                print("無此值\n======================")
                
        elif value>cur_value.value:
            if cur_value.right:
                self.__delete(value,cur_value.right)
            else:
                print("無此值\n======================")
                
        elif value==self.root.value:#刪除的子節點為根節點
                if cur_value.left==None and cur_value.right==None:#根節點沒有子節點
                    self.root=None
                    cur_value=None
                    print("刪除完畢，目標為根節點") 
                    print("此二元搜尋樹無節點\n======================")
                    
                elif cur_value.left==None and cur_value.right:#只有右子節點
                    self.root=cur_value.right
                    cur_value.right.parent=None
                    cur_value=None
                    print("刪除完畢，目標為根節點")
                    print("已保留右子節點\n======================")
                    
                elif cur_value.left and cur_value.right==None:#只有左子節點
                    self.root=cur_value.left
                    cur_value.left.parent=None
                    cur_value=None
                    print("刪除完畢，目標為根節點\n======================")
                """            
                else:#根節點有左右子節點
                
                    cur_value=None
                    print("刪除完畢，目標為根節點\n======================")
                """
                
        elif value==cur_value.value:#找到值
        #需考慮刪除的節點的左右節點是否有子節點，因此只更改父節點的指向
            #print("cur_value:",cur_value.value)
            if cur_value.left==None and cur_value.right==None:#沒有子節點
                if cur_value.parent.value<cur_value.value:#父節點的值小於目標值，即目標值在父節點的右邊
                    cur_value.parent.right=None
                elif cur_value.parent.value>cur_value.value:#父節點的值大於目標值，即目標值在父節點的左邊
                    cur_value.parent.left=None
                cur_value=None
                print("刪除完畢，目標沒有子節點\n======================")
            
            elif cur_value.left==None and cur_value.right:#只有右子節點
                
                if cur_value.parent.value<cur_value.value:#父節點的值小於目標值，即目標值在父節點的右邊
                    cur_value.parent.right=cur_value.right
                    cur_value.right.parent=cur_value.parent
                elif cur_value.parent.value>cur_value.value:#父節點的值大於目標值，即目標值在父節點的左邊
                    cur_value.parent.left=cur_value.right
                    cur_value.right.parent=cur_value.parent
                    
                cur_value=None
                print("刪除完畢，目標含右節點\n======================")
               
            elif cur_value.left and cur_value.right==None:#只有左子節點
                if cur_value.parent.value<cur_value.value:#父節點的值小於目標值，即目標值在父節點的右邊
                    cur_value.parent.right=cur_value.left
                    cur_value.left.parent=cur_value.parent
                elif cur_value.parent.value>cur_value.value:#父節點的值大於目標值，即目標值在父節點的左邊
                    cur_value.parent.left=cur_value.left
                    cur_value.left.parent=cur_value.parent
                cur_value=None
                print("刪除完畢，目標含左節點\n======================")
                 
            """        
            else:#有左右子節點
                
                cur_value=None
                print("刪除完畢，目標含左右節點\n======================")
            
            """     
    
    def print_tree(self):
        if self.root!=None:
        	self._print_tree(self.root)
        print("列印完畢\n======================")
        
    def _print_tree(self,cur_node):
    	if cur_node!=None:
        	self._print_tree(cur_node.left)
        	print(str(cur_node.value))
        	self._print_tree(cur_node.right)
            
            
        
            
        
            
            
b=BST()

lists=[10,5,7,3,8,2,]#
for _ in lists:
    b.insert(_)

b.print_tree()
b.delete(3)
b.print_tree()
