import rubik
from rubik import *
import time
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
    if start==end:return []
    startparent = {}
    endparent = {}
    visitedstart = set()
    visitedend = set()
    startq = deque()
    startq.append(start)
    endq = deque()
    endq.append(end)
    startdist = {start: 0}
    enddist = {end: 0}
    f = 0
    while startq or endq:
        if startq:
            curr = startq.popleft()

            for move in rubik.quarter_twists:
                neigh = rubik.perm_apply(move, curr)
                if neigh in startdist.keys():
                    if startdist[neigh] > startdist[curr] + 1:
                        startdist[neigh] = startdist[curr] + 1
                        startparent[neigh] = tuple([curr, move])
                        startq.append(neigh)
                else:
                    startdist[neigh] = startdist[curr] + 1
                    startparent[neigh] = tuple([curr, move])
                    startq.append(neigh)
            visitedstart.add(curr)
        if curr in visitedend and curr in visitedstart:
            f = 1
            print("Start wale se")
            break

        if endq:
            curr = endq.popleft()
            for move in rubik.quarter_twists:
                neigh = rubik.perm_apply(move, curr)
                if neigh in enddist.keys():
                    if enddist[neigh] > enddist[curr] + 1:
                        enddist[neigh] = enddist[curr] + 1
                        endparent[neigh] = tuple([curr, move])
                        endq.append(neigh)

                else:
                    enddist[neigh] = enddist[curr] + 1
                    endparent[neigh] = tuple([curr, move])
                    endq.append(neigh)
            visitedend.add(curr)

        # check if visited
        if (curr in visitedend) and (curr in visitedstart):
            # print(len(endq), len(startq))
            f = 1
            # print("End wale se")
            break
    if f:
        quarter_twists_inverse = {F: Fi, L: Li, U: Ui, Fi: F, Li: L, Ui: U}
        # print(start)
        # print(curr)
        # print(end)
        movestostart = [rubik.quarter_twists_names[startparent[curr][1]]]
        parent = startparent[curr][0]
        while (parent != start):
            movestostart.append(quarter_twists_names[startparent[parent][1]])
            parent = startparent[parent][0]
        movestoend = []
        if curr != end:
            # print(curr)
            # endparent[curr][1]
            # print(endparent[curr][1])
            movestoend = [rubik.quarter_twists_names[quarter_twists_inverse[endparent[curr][1]]]]
            parent = endparent[curr][0]
            while (parent != end):
                movestoend.append(rubik.quarter_twists_names[quarter_twists_inverse[endparent[parent][1]]])
                parent = endparent[parent][0]
        return movestostart[::-1] + movestoend



start = time.time()
path = shortest_path((6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
end  = time.time()


print("PATH:"+str(path))
print("time in secs:" + str(end - start))


start = time.time()
path = shortest_path_optmized((6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
end  = time.time()


print("PATH:"+str(path))
print("time in secs:" + str(end - start))