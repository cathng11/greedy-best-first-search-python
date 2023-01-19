from Graph import Node, Graph
import heapq
import pandas as pd
graph = [[] for i in range(15)]


def GBFS(initialState, goalTest, n):
    explored = [0 for i in range(n)]
    frontier = []
    result = []
    frontier = [initialState]
    explored[initialState] = 1
    print(frontier)

    print(frontier)
    while len(frontier) > 0:
        node = frontier.pop(0)
        result.append(node)
        for x in range(0, len(graph[node])):
            if (int(explored[int(graph[node][x])]) == 0):
                explored[int(graph[node][x])] = 1
                frontier.append(int(graph[node][x]))
                print(frontier)
        if frontier[0] == goalTest:
            break
        else:
            addlist = []
            minfr = cost[frontier[0]]
            for i in frontier:
                addlist.append([i, cost[i]])
                if(minfr >= cost[i]):
                    minfr = cost[i]
            addlist = sorted(addlist, key=lambda x: x[1])
            for j in range(0, len(addlist)):
                frontier[j] = addlist[j][0]
                print(frontier)


def addEgde(x, y):
    graph[x].append(y)
    graph[y].append(x)


addEgde(0, 1)
addEgde(0, 2)
addEgde(0, 3)
addEgde(1, 4)
addEgde(1, 5)
addEgde(2, 6)
addEgde(2, 7)
addEgde(3, 8)
addEgde(3, 9)
addEgde(5, 10)
addEgde(5, 11)
addEgde(5, 12)
addEgde(7, 13)
addEgde(7, 14)

cost = [6, 3, 4, 3, 1, 6, 2, 5, 4, 2, 0, 4, 0, 4]

GBFS(0, 2, 15)
