

class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList(object):#index:head=0,head的下一個為1,類推

    def __init__(self):
        self.head=Node(None)
        self.tail=None
        self.head.next=self.tail
        self.length=0
    
    def get(self, index):
        """
        return value of index
        :type index: int
        
        :rtype: int
        """
        if index<0 or index>=self.length:
            return -1
        
        cur=self.head
        cur_index=0
        while cur_index-1!=index:#因為第一個是head=None,所以要-1
            
            cur=cur.next
            cur_index+=1
        
        return cur.val


    def addAtHead(self, val):#
        """
        :type val: int
        :rtype: None
        """
        add_head=Node(val)
        add_head.next=self.head.next
        self.head.next=add_head
        self.length+=1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        add_tail=Node(val)
        add_tail.next=self.tail
        cur_node=self.head       
        print("tail:",add_tail.val)
        while cur_node.next!=None:#讓cur檢測下一個是不是tail
            
            cur_node=cur_node.next
            
        cur_node.next=add_tail    
        self.length+=1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index<0 or index>self.length:
            return 
        
        """
        if index==0:
            self.addAtHead(val)
        """
        
        cur_index=-1
        cur_node=self.head
        new_node=Node(val)
        previous_node=cur_node
        
        while cur_index!=index:
            previous_node=cur_node
            cur_node=cur_node.next
            cur_index+=1
            
        new_node.next=cur_node
        previous_node.next=new_node
        self.length+=1
        return None
        
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.length:
            return -1
        
        cur_index=0
        cur_node=self.head.next
        previous_node=self.head 
    
        while cur_index+1<=index:
            previous_node=previous_node.next
            cur_node=cur_node.next
            cur_index+=1

        previous_node.next=cur_node.next
        
        cur_node=None
        self.length-=1

# 測試步驟
operations =["MyLinkedList","addAtHead","addAtIndex","addAtIndex","addAtHead","deleteAtIndex","addAtIndex","addAtHead","addAtTail","addAtHead","get","addAtTail","addAtTail","addAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","addAtHead","addAtTail","addAtHead","addAtTail","addAtTail","addAtHead","addAtTail","addAtIndex","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtIndex","addAtHead","addAtTail","addAtHead","deleteAtIndex","addAtTail","deleteAtIndex","addAtTail","addAtTail","addAtTail","addAtTail","addAtHead","addAtTail","get","addAtIndex","get","deleteAtIndex","addAtTail","addAtHead","addAtTail","addAtTail","addAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","deleteAtIndex","deleteAtIndex","addAtHead","addAtHead","addAtTail","addAtHead","get","addAtIndex","addAtIndex","get","addAtTail","get","addAtTail","deleteAtIndex","get","addAtTail","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtHead","deleteAtIndex","addAtTail","addAtIndex","addAtTail","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtIndex","addAtHead","addAtHead","addAtTail","addAtIndex","addAtTail","get","addAtHead","addAtTail","addAtHead","addAtHead"]



values=[[],[86],[1,54],[1,14],[83],[4],[3,18],[46],[3],[76],[5],[79],[74],[7,28],[68],[16],[82],[24],[30],[96],[21],[79],[66],[2],[2],[7,57],[59],[21],[19],[55],[46],[17],[16,41],[97],[85],[63],[30],[11],[16],[91],[29],[47],[20],[12],[80],[15],[12,8],[21],[30],[11],[54],[51],[41],[8,88],[62],[7],[59],[73],[73],[55],[9],[7],[49],[99],[17],[44],[11],[26,86],[10,99],[19],[71],[29],[32],[2],[3],[16],[2],[83],[31],[3],[23],[64],[96],[27],[81],[12,78],[21],[69],[5,35],[8,72],[60],[19,73],[55],[83],[86],[31,70],[49],[19],[64],[22],[25],[13]]


#output:[null,null,null,null,null,null,null,null,null,null,18,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,57,null,28,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,46,null,null,30,null,41,null,null,73,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,97,null,null,null,null]
# 執行測試步驟
linked_list = None
results = []

for i in range(len(operations)):
    print("現在是第:,",i)
    operation = operations[i]
    value = values[i]

    if operation == "MyLinkedList":
        linked_list = MyLinkedList()
        print("MyLinkedList")
        results.append(None)
    elif operation == "addAtHead":
        linked_list.addAtHead(value[0])
        print("-------\naddAtHead")
        results.append(None)
    
    elif operation == "addAtIndex":
        linked_list.addAtIndex(value[0], value[1])
        print("-------\naddAtIndex")
        results.append(None)    
    
    elif operation == "addAtTail":
        linked_list.addAtTail(value[0])
        print("-------\naddAtTail")
        results.append(None)
    elif operation == "get":
        print("-----\nget")
        result = linked_list.get(value[0])
        print("-------\nget:",result)
        results.append(result)
    elif operation == "deleteAtIndex":
        linked_list.deleteAtIndex(value[0])
        print("-------\ndeleteAtIndex:",value[0])
        results.append(None)
        
    for i in range(0,20):
        print("現在串列內容:",linked_list.get(i))
print(results)

