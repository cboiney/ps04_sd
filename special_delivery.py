#main file for special_delivery project

#for max integer
import sys

#returns the optimal sequence for a subproblem
def sd_helper(distances, weights, position, visited, weight):
    #check if we've already visited everything, if so we can return empty
    finished = True
    for v in range(0, len(visited)):
        if (visited[v] == 0):
            finished = False
            break
    if (finished):
        return (0, [])
    #default choice is the first one (completely arbitrary, we know we will find something unvisited)
    choice = 0
    #set best very high! 
    #CITE: https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
    best = sys.maxsize
    #initialize the array representing the rest of the choices
    rest = []
    for v in range(0, len(visited)):
        #if we haven't delivered the package at stop v, try it
        if (visited[v] == 0):
            #create duplicate visit record
            #CITE: https://stackoverflow.com/questions/66585998/making-a-copy-of-an-array-in-python
            tmp = visited.copy()
            tmp[v] = 1
            #solve sub problem
            result = sd_helper(distances, weights, v, tmp, weight-weights[v])
            #compute cost of this choice (distance to stop + optimal cost from there)
            cost = weight*(abs(v-position) + distances[v]) + result[0]
            #if we have a new best choice, update
            if (cost < best):
                best = cost
                choice = v
                rest = result[1]
    #return the cost of the best choice, as well as the new array with the updated choice
    return (best, [(choice+1)] + rest)
    

    

#returns the optimal sequence of deliveries for a given set of locations and distances
def special_delivery(distances, weights):
    n = len(distances)
    visited = [0] * n
    #start at -1 since it takes 1 step to get to the first stop, and we use 0 indexing
    results = sd_helper(distances, weights, -1, visited, sum(weights))
    output = ""
    for i in range(0, n):
        output += str(results[1][i])
        if (i+1 < n):
            output += " "
    return output

#run the program on a given file, returns an array containing all solutions
def run_file(file):
    #open the file, pull out the lines
    with open(file, 'r') as file:
        lines = []
        for line in file:
            stripped = line.strip()
            split = stripped.split()
            lines.append(split)

        distances = []
        weights = []

        for line in lines:
            distances.append(int(line[0]))
            weights.append(int(line[1]))

        return special_delivery(distances, weights)