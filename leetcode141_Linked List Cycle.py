# Definition for singly-linked list.
#import time

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        透過記錄已有的節點的記憶體位置，
        若某次的next指向其一元素，即circle
        """
        
        recorder=[]
        new_node=head
        
        if new_node==None:
            return False

        while new_node.next!=None:
            #print("val:",new_node.val)
            if new_node.next in recorder:
                return True
            else:
                recorder.append(new_node)
                new_node=new_node.next
                #print(recorder)
                #time.sleep(5)
                continue
                
        return False
            
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# 連結節點形成鏈表
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # 此處形成循環

# 測試
result = Solution()
result.hasCycle(node1)
print(result)  # 輸出: Tru