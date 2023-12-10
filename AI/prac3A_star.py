def sort(priorityQueue):
    for x,values in enumerate(priorityQueue):
        y=0
        while(y<len(priorityQueue)-x-1):
            if(priorityQueue[y][1]>priorityQueue[y+1][1]):
                t=priorityQueue[y]
                priorityQueue[y]=priorityQueue[y+1]
                priorityQueue[y+1]=t
            y+=1
    return priorityQueue            

def functionValue(newState,heuristicValue,pathCost):
    value=0
    x=0
    while x<len(newState):
        if x==len(newState)-1:
            value+=heuristicValue.get(newState[x])
            break    
        else:
            for z in pathCost:
                if(newState[x]==z[0] and newState[x+1]==z[1]):
                    value+=z[2]
                    break
            x+=1  
    return value       
   
def displayPath(path):
    print(" --> ".join(path))
    return("")

def A_star(priorityQueue,edges,heuristicValue,pathCost,goal):
    priorityQueue=sort(priorityQueue)
    if(priorityQueue[0][0][-1]==goal):
        print("\nThe most optimal path to reach goal is:\n")
        print(displayPath(priorityQueue[0][0]))
        print("Total cost = ",priorityQueue[0][1])
        return
    for i in edges:
        if(i==priorityQueue[0][0][-1]):
            for j in edges[i]:
                newState=priorityQueue[0][0][:]
                newState.append(j)
                value=functionValue(newState,heuristicValue,pathCost)
                priorityQueue.append([newState,value])
            priorityQueue.pop(0)    
            break
    A_star(priorityQueue,edges,heuristicValue,pathCost,goal)        

edges={
    "A":["B","C","D"],
    "B":["E"],
    "C":["E","F"],
    "D":["F"],
    "E":["H"],
    "F":["G"],
    "H":["G"]
}
start="A"
goal="G"
heuristicValue={
    "A":40,
    "B":32,
    "C":25,
    "D":35,
    "E":19,
    "F":17,
    "H":10,
    "G":0
}
pathCost=[
    ["A","B",11],
    ["A","C",14],
    ["A","D",7],
    ["B","E",15],
    ["C","E",8],
    ["C","F",10],
    ["D","F",25],
    ["E","H",9],
    ["F","G",20],
    ["H","G",10]
]
priorityQueue=[[[start],heuristicValue.get("A")]]
A_star(priorityQueue,edges,heuristicValue,pathCost,goal)