import numpy as np
import matplotlib.pyplot as plt

def Astar(map, start, end):
        '''
        :param map: A 2D numpy array of representing the world's cspace with 0 as free space and 1 as obstacle
        :param start: A tuple of indices representing the start cell in the map
        :param end: A tuple of indices representing the end cell in the map
        :return: A list of tuples as a path from the given start to the given end in the given maze
        '''
        prev = {start: None}
        costs = {start: 0}
        explored = {}
        
        def f(n):
            return np.sqrt((end[0]-n[0])**2+(end[1]-n[1])**2)+costs[n]

        def getAdjacent(x, y):
            newCoords, newPosCoords = [], [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
            for coord in newPosCoords:
                if isValidAdjacent(coord[0], coord[1]):
                    newCoords.append(coord)
            return newCoords

        def isValidAdjacent(x, y):
            return (0 < x and x < map.shape[1]) and (0 < y and y < map.shape[0])

        q = [(start, f(start))]
        while len(q) != 0:
            lowIndex, lowest = 0, q[0][1]
            for x in range(len(q)):
                if q[x][1] < lowest:
                    lowIndex, lowest = x, q[x][1]

            current = q.pop(lowIndex) #current is of the type ((x,y), cost)
            current, cost = current
            explored[current] = None
        
            if current == end:
                finalPath = []
                finalPath.append(end)
                previous = prev[current]
                while previous is not None:
                    finalPath.append(previous)
                    previous = prev[previous]
                finalPath.reverse()
                return finalPath
            else:      ## non-obstacle state check
                newStates = getAdjacent(current[0], current[1])
                for state in newStates:   #check all adjacent states and add to q with correct
                    if state not in explored and map[state[1]][state[0]] == 0:
                        state_cost = cost + 1
                        if state not in costs or state_cost < costs[state]:
                            prev[state], costs[state] = current, state_cost
                            q.append((state, f(state)))
        print('Cannot reach goal')
        return []