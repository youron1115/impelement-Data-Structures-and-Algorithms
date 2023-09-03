
class Graph_DIY():#無向圖
    def __init__(self,graph=None):
        if graph == None:#若一開始沒給圖就給一個空的圖
            graph = {}
        self.graph_dict = graph
        #載入圖

    def get_point(self):#回傳point(or vertex)
        return list(self.graph_dict.keys())
      
    def add_point(self,point):#增加新的點,print處顯示是否成功
        print("舊的點")
        print(self.get_point())
        if point not in self.graph_dict:
            self.graph_dict[point] = []#將新頂點以字典形式加入圖中，但無連接其他點
            #增加點
        print("新的點")
        print(self.get_point())
        
    def get_edge(self):
        edge = []#回傳的邊將以list形式呈現
        for point in self.graph_dict:#point為graph_dict的key
            for next_point in self.graph_dict[point]:#next_point為graph_dict的value
                if {next_point,point} not in edge:#這個條件使得edge中的元素不會重複
                    edge.append({point,next_point})
        return edge
    
    def add_edge(self,main_point,to_point):#增加邊,print處顯示是否成功
        print("舊的邊")
        print(self.get_edge())
        for point in self.graph_dict:
            if point == main_point:
                self.graph_dict[point].append(to_point)
        print("新的邊")
        print(self.get_edge())
        
def DFS(g_dict,start,visited = None):
    if visited == None:#先確認有無預設值visited
        visited = set()
        
        print('start:',start)
        print('visited:',visited)
        
    visited.add(start)#將起始點加入visited
        
    for next in set(g_dict[start]) - visited:#差集操作(需兩者階級和型態)，藉此得到尚未訪問過的相鄰節點
        DFS(g_dict, next, visited)
    #print("visited:",visited)
    return visited

#DFS(graphs,'A')

def BFS(g_dict,start):
    
    if g_dict == None:
        g_dict = {}
    
    #print("\nstart:",start)
    visited = set(start)
    my_queue =[]
    my_queue.append(start)
    
    while my_queue:
        for i in g_dict[my_queue[0]]:
            if i not in my_queue and i not in visited:
                my_queue.append(i)
        visited.add(my_queue[0])
        del my_queue[0]
        print("visited:",visited)
        print("queue:",my_queue)
    
#BFS(graphs,'A')    
    
       
 
graphs={
        'A':['B','C'],
        'B':['A','D','E'],
        'C':['A','F'],
        'D':['B','G'],
        'E':['B','G'],
        'F':['C','H'],
        'G':['D','E','I'],
        'H':['F','I'],
        'I':['G','H']
      }



