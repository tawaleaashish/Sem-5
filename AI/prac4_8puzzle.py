import copy
def manhattanDist(currentState,path):
    goalState=[[1,2,3],[4,5,6],[7,8,0]]
    dist=0
    flag=0
    x=0
    y=0
    for i,row in enumerate(currentState):
        for j,col in enumerate(row):
            while(x<len(goalState)):
                while(y<len(goalState[x])):
                    if(col==0):
                        x=0
                        y=0
                        flag=1
                        break
                    if(col==goalState[x][y]):
                        value=max(i,x)-min(i,x)+max(j,y)-min(j,y)
                        dist+=value
                        x=0
                        y=0
                        flag=1
                        break
                    y+=1
                if(flag==1):
                    flag=0
                    break
                y=0
                x+=1
    dist+=(len(path)-1)            
    return dist 
               
def display(state):
    for i,row in enumerate(state):
        for j,col in enumerate(row):
            if (j<2):
                if(col==0):
                    print(""," ","|",end="")
                else:
                    print("",col,"|",end="")      
            else:
                if(col==0):
                    print(""," ")    
                else:
                    print("",col)    

        if(i<2):
            print("-----------")  

def sort(states):
    i=0
    j=0
    while(i<len(states)):
        while(j<len(states)-i-1):
            if(states[j][1]>states[j+1][1]):
                t=states[j]
                states[j]=states[j+1]
                states[j+1]=t
            j+=1
        j=0    
        i+=1
    return states            

def swaps(state,i,j,path,States,visited):
    n=copy.deepcopy(state)
    p=copy.deepcopy(path)
    if (i-1)>=0:
        t=n[i][j]
        n[i][j]=n[i-1][j]
        n[i-1][j]=t
        if(n not in visited):
            p.append(n)
            States.append([copy.deepcopy(p),manhattanDist(n,p)])
            p=copy.deepcopy(path)
        n=copy.deepcopy(state)
    if (i+1)<3:
        t=n[i][j]
        n[i][j]=n[i+1][j]
        n[i+1][j]=t
        if(n not in visited):
            p.append(n)
            States.append([copy.deepcopy(p),manhattanDist(n,p)])
            p=copy.deepcopy(path)
        n=copy.deepcopy(state)
    if (j-1)>=0:
        t=n[i][j]
        n[i][j]=n[i][j-1]
        n[i][j-1]=t
        if(n not in visited):
            p.append(n)
            States.append([copy.deepcopy(p),manhattanDist(n,p)])
            p=copy.deepcopy(path)
        n=copy.deepcopy(state)
    if (j+1)<3:
        t=n[i][j]
        n[i][j]=n[i][j+1]
        n[i][j+1]=t
        if(n not in visited):
            p.append(n)
            States.append([copy.deepcopy(p),manhattanDist(n,p)])
            p=copy.deepcopy(path)
        n=copy.deepcopy(state)
    return States    


def NewState(state,path,States,visited):
    for i,row in enumerate(state):
        for j,col in enumerate(row):
            if(col==0):
                States=swaps(state,i,j,path,States,visited)
                return States           


initialState=[[6,1,2],[4,8,7],[5,0,3]]
goalState=[[1,2,3],[4,5,6],[7,8,0]]
visited=[]
States=[[[initialState],manhattanDist(initialState,[initialState])]]
while True:
    States=sort(States)
    if(States[0][0][-1]==goalState):
        for a,s in enumerate(States[0][0]):
            print("Step ",a,"\n")
            display(s)
            print("\n")
        print("\nGoal state acheived.")
        break
    else:
        for v in States:
            if(v[0][-1] not in visited):
                    visited.append(v[0][-1])
        p=States.pop(0)
        States=NewState(p[0][-1],p[0],States,visited)