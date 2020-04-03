import rubik
import timeit
from collections import deque
def shortest_path(start, end):
    """
    For Question 1, using BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """ 
    visited = {}
    
    visited[start] = (start,-1)
    config = []
    nodes = deque()
    nodes.append(start)
    while nodes:
        node = nodes.popleft()
        if node == end:
            break
        else:
            for i in rubik.quarter_twists:
                temp_node = rubik.perm_apply(node,i)
                if (not(visited.__contains__(temp_node))):
                    visited[temp_node]=(node,rubik.quarter_twists_names[i])
                    nodes.append(temp_node)
                else:
                    continue
                    

    if(len(visited)==1):
        return []
    if(visited.__contains__(end)):
        rev_config = deque()
        config = []
        temp_node = end
        while (temp_node!= start):
            temp_node,temp = visited[temp_node]
            rev_config.append(temp)
        while(rev_config):
            config.append(rev_config.pop())
        return config
    else:
        return None


    


def shortest_path_optmized(start, end):
    """
    For Question 2, using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    raise NotImplementedError

start = timeit.timeit()
path = shortest_path((6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
end  = timeit.timeit()
print("PATH:"+str(path))
print("time in secs:" + str(end - start))