def displayPath(path,goal):
    print("\nThe Path to reach Goal state using Best First Search is :")
    for p in path:
        if p!=goal:
            print(p+" --> ",end="")
        else:
            print(p)    

def sort(priorityQueue,heuristicValue):
    sortlist=[]
    for a in priorityQueue:
        for b in heuristicValue:
            if(b==a):
                sortlist.append([a,heuristicValue[b]])
                break    
    for x,value in enumerate(sortlist):
        y=0
        while y<len(sortlist)-x-1:
            if(sortlist[y+1][1]<sortlist[y][1]):
                t=sortlist[y+1]
                sortlist[y+1]=sortlist[y]
                sortlist[y]=t
            y+=1

    for a,value in enumerate(priorityQueue):
        priorityQueue[a]=sortlist[a][0]
    return priorityQueue              

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
priorityQueue=[start]
path=[]

while len(priorityQueue)>0:
    node=priorityQueue.pop(0)
    path.append(node)
    if node==goal:
        displayPath(path,goal)
        break
    else:
        for j in edges:
            if(j==node):
                priorityQueue.clear()
                for k in edges[j]:
                    priorityQueue.append(k)
                break             
        priorityQueue=sort(priorityQueue,heuristicValue)  